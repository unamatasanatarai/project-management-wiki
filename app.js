(() => {
    "use strict";

    const state = {
        terms: [],
        termsBySlug: {},
        query: "",
        currentView: null
    };

    const app = document.getElementById("app");
    const searchInput = document.getElementById("searchInput");
    const clearSearchBtn = document.getElementById("clearSearch");
    const randomBtn = document.getElementById("randomBtn");

    async function initialize() {
        try {
            const response = await fetch("data/terms.json");

            if (!response.ok) {
                throw new Error(
                    `Nie można załadować danych (${response.status})`
                );
            }

            const data = await response.json();

            if (!data || !Array.isArray(data.terms)) {
                throw new Error(
                    "Nieprawidłowy format terms.json"
                );
            }

            state.terms = data.terms;

            state.termsBySlug = Object.fromEntries(
                state.terms.map(term => [
                    term.slug,
                    term
                ])
            );

            // Setup placeholder text based on screen size
            updatePlaceholder();
            window.addEventListener("resize", updatePlaceholder);

            // Bind global events
            document.body.addEventListener("click", handleGlobalClick);
            window.addEventListener("hashchange", renderRoute);
            window.addEventListener("keydown", handleGlobalKeyDown);

            // Bind search input events
            searchInput.addEventListener("input", handleSearchInput);
            clearSearchBtn.addEventListener("click", handleClearSearch);
            searchInput.addEventListener("keydown", handleSearchKeyDown);
            randomBtn.addEventListener("click", handleRandomClick);

            renderRoute();

        } catch (error) {
            console.error(error);
            renderError(
                error.message || "Nie udało się załadować aplikacji."
            );
        }
    }

    function updatePlaceholder() {
        const isMobile = window.matchMedia("(max-width: 767px)").matches;
        searchInput.placeholder = isMobile ? "Szukaj pojęcia..." : "Szukaj pojęcia... (naciśnij /)";
    }

    function handleGlobalKeyDown(event) {
        if (event.key === "/") {
            const active = document.activeElement;
            const isInput = active.tagName === "INPUT" ||
                active.tagName === "TEXTAREA" ||
                active.isContentEditable;

            // Disable shortcut on mobile viewports altogether
            const isMobile = window.matchMedia("(max-width: 767px)").matches;
            if (!isInput && !isMobile) {
                event.preventDefault();
                searchInput.focus();
                searchInput.select();
            }
        }
    }

    function handleSearchKeyDown(event) {
        if (event.key !== "Enter") {
            return;
        }

        event.preventDefault();

        const firstCard = document.querySelector(
            "#resultsContainer .card"
        );

        if (!firstCard) {
            return;
        }

        const slug = firstCard.dataset.slug;

        if (slug) {
            location.hash = `#/term/${slug}`;
        }
    }

    function handleSearchInput(event) {
        state.query = event.target.value;
        updateClearButtonVisibility();

        renderResults();
    }

    function handleRandomClick() {
        if (!state.terms || state.terms.length === 0) {
            return;
        }

        const randomIndex = Math.floor(Math.random() * state.terms.length);
        const randomTerm = state.terms[randomIndex];

        if (randomTerm && randomTerm.slug) {
            location.hash = `#/term/${randomTerm.slug}`;
        }
    }

    function handleClearSearch() {
        state.query = "";
        searchInput.value = "";
        updateClearButtonVisibility();
        searchInput.focus();

        renderResults();
    }

    function updateClearButtonVisibility() {
        if (state.query.trim().length > 0) {
            clearSearchBtn.style.display = "flex";
        } else {
            clearSearchBtn.style.display = "none";
        }
    }

    function renderRoute() {
        const hash = location.hash || "#/";

        // Keep search input value synced
        if (searchInput.value !== state.query) {
            searchInput.value = state.query;
        }

        updateClearButtonVisibility();
        renderResults();

        if (hash.startsWith("#/term/")) {
            const slug = decodeURIComponent(
                hash.replace("#/term/", "")
            );
            renderTerm(slug);
            app.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        } else {
            renderWelcome();
        }
    }

    function normalizeText(text) {
        return (text || "")
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");
    }

    function getSearchScore(term, query) {
        if (!query) return 1;

        const q = normalizeText(query);

        const title = normalizeText(term.title);
        const category = normalizeText(term.category);
        const description = normalizeText(term.description);
        const search = normalizeText(term.search);

        let score = 0;

        // Exact title match
        if (title === q) {
            score += 10000;
        }

        // Title starts with query
        else if (title.startsWith(q)) {
            score += 5000;
        }

        // Title contains query
        else if (title.includes(q)) {
            score += 3000;
        }

        // Multi-word relevance
        const words = q.split(/\s+/).filter(Boolean);

        for (const word of words) {
            if (title.includes(word)) {
                score += 500;
            }

            if (category.includes(word)) {
                score += 100;
            }

            if (description.includes(word)) {
                score += 50;
            }

            if (search.includes(word)) {
                score += 10;
            }
        }

        // Related terms
        if (
            term.related?.some(
                item =>
                    normalizeText(item.title).includes(q) ||
                    normalizeText(item.slug).includes(q)
            )
        ) {
            score += 250;
        }

        // Category direct match
        if (category.includes(q)) {
            score += 200;
        }

        // Description direct match
        if (description.includes(q)) {
            score += 100;
        }

        // Search index fallback
        if (search.includes(q)) {
            score += 25;
        }

        return score;
    }

    function renderResults() {
        const resultsContainer = document.getElementById("resultsContainer");
        const resultsMeta = document.getElementById("resultsMeta");

        if (!resultsContainer || !resultsMeta) {
            return;
        }

        const query = state.query.trim();

        let results;

        if (!query) {
            results = [...state.terms];
        } else {
            results = state.terms
                .map(term => ({
                    term,
                    score: getSearchScore(term, query)
                }))
                .filter(item => item.score > 0)
                .sort((a, b) => {
                    if (b.score !== a.score) {
                        return b.score - a.score;
                    }

                    return a.term.title.localeCompare(
                        b.term.title,
                        "pl"
                    );
                })
                .map(item => item.term);
        }

        resultsMeta.textContent = results.length;

        if (results.length === 0) {
            resultsContainer.innerHTML = `
            <div class="empty">
                Nie znaleziono żadnych wyników.
            </div>
        `;
            return;
        }

        resultsContainer.innerHTML = results
            .map(renderCard)
            .join("");

        highlightActiveCard();
    }

    function highlightActiveCard() {
        const hash = location.hash || "#/";
        let activeSlug = "";
        if (hash.startsWith("#/term/")) {
            activeSlug = decodeURIComponent(hash.replace("#/term/", ""));
        }

        document.querySelectorAll(".card").forEach(card => {
            if (card.dataset.slug === activeSlug) {
                card.classList.add("active");
            } else {
                card.classList.remove("active");
            }
        });
    }

    function renderCard(term) {
        return `
            <article
                class="card"
                data-slug="${escapeHtml(term.slug)}"
                tabindex="0"
                role="button"
                aria-label="Otwórz ${escapeHtml(term.title)}"
            >
                <h2 class="card-title">
                    ${escapeHtml(term.title)}
                </h2>
                <p class="card-description">
                    ${escapeHtml(term.description || "")}
                </p>
                <div class="badge">
                    ${escapeHtml(term.category || "")}
                </div>
            </article>
        `;
    }

    function renderWelcome() {
        state.currentView = "dictionary";
        document.body.setAttribute("data-view", "dictionary");

        app.innerHTML = `
            <div class="empty-state-welcome">
                <h2>Słownik Project Management</h2>
                <p>Wyszukaj pojęcie lub wybierz je z listy, aby zobaczyć szczegóły.</p>
            </div>
        `;

        updateSEO();
    }

    function renderTerm(slug) {
        state.currentView = "term";
        document.body.setAttribute("data-view", "term");

        const term = state.termsBySlug[slug];

        if (!term) {
            renderNotFound();
            return;
        }

        const relatedSection = term.related && term.related.length
            ? `
            <section class="related-section">
                <h2>Powiązane pojęcia</h2>
                <div class="related-list">
                    ${term.related
                .map(item => `
                            <a
                                class="related-link"
                                href="#/term/${item.slug}"
                            >
                                ${escapeHtml(item.title)}
                            </a>
                        `)
                .join("")}
                </div>
            </section>
            `
            : "";

        app.innerHTML = `
            <article class="article">
                <a href="#/" class="back-link">
                    ← Powrót do słownika
                </a>

                <header class="article-header">
                    <h1>
                        ${escapeHtml(term.title)}
                    </h1>
                    <div class="badge">
                        ${escapeHtml(term.category || "")}
                    </div>
                </header>

                <section class="article-content">
                    ${term.content || ""}
                </section>

                ${relatedSection}
            </article>
        `;

        highlightActiveCard();
        updateSEO(term.title, term.description);
        renderMath(app);
    }

    function renderError(message) {
        state.currentView = "error";
        document.body.setAttribute("data-view", "error");

        app.innerHTML = `
            <div class="error">
                <h2>Błąd</h2>
                <p>${escapeHtml(message)}</p>
            </div>
        `;

        updateSEO("Błąd");
    }

    function renderNotFound() {
        state.currentView = "notfound";
        document.body.setAttribute("data-view", "notfound");

        app.innerHTML = `
            <div class="error">
                <h2>Nie znaleziono wpisu</h2>
                <p>Podane pojęcie nie istnieje.</p>
                <a href="#/">Wróć do słownika</a>
            </div>
        `;

        updateSEO("Nie znaleziono wpisu");
    }

    function handleGlobalClick(event) {
        const card = event.target.closest(".card");
        if (!card) {
            return;
        }

        const slug = card.dataset.slug;
        if (!slug) {
            return;
        }

        location.hash = `#/term/${slug}`;
    }

    function updateSEO(title, description) {
        const pageTitle = title ? `${title} - Project Management - Ściąga` : "Project Management - Ściąga";
        const pageDesc = description || "Interaktywny słownik pojęć i narzędzi z zakresu Project Management. Definicje, przykłady i powiązania w jednym miejscu.";

        document.title = pageTitle;

        const setMeta = (selector, attr, value) => {
            const el = document.querySelector(selector);
            if (el) el.setAttribute(attr, value);
        };

        setMeta('meta[name="description"]', 'content', pageDesc);
        setMeta('meta[property="og:title"]', 'content', pageTitle);
        setMeta('meta[property="og:description"]', 'content', pageDesc);
        setMeta('meta[property="og:url"]', 'content', window.location.href);
        setMeta('meta[name="twitter:title"]', 'content', pageTitle);
        setMeta('meta[name="twitter:description"]', 'content', pageDesc);
    }

    function renderMath(container) {
        if (typeof renderMathInElement === "function") {
            renderMathInElement(container, {
                delimiters: [
                    { left: "$$", right: "$$", display: true },
                    { left: "$", right: "$", display: false }
                ],
                throwOnError: false
            });
        } else {
            // KaTeX not yet loaded – wait and retry once
            window.addEventListener("load", () => renderMath(container), { once: true });
        }
    }

    function escapeHtml(value) {
        const div = document.createElement("div");
        div.textContent = value ?? "";
        return div.innerHTML;
    }

    initialize();
})();
