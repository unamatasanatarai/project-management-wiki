(() => {
    "use strict";

    const state = {
        terms: [],
        termsBySlug: {},
        query: "",
        currentView: null
    };

    const app = document.getElementById("app");

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

            app.addEventListener(
                "click",
                handleGlobalClick
            );

            window.addEventListener(
                "hashchange",
                renderRoute
            );

            renderRoute();

        } catch (error) {

            console.error(error);

            renderError(
                error.message ||
                "Nie udało się załadować aplikacji."
            );
        }
    }

    function renderRoute() {

        const hash = location.hash || "#/";

        if (hash.startsWith("#/term/")) {

            const slug = decodeURIComponent(
                hash.replace("#/term/", "")
            );

            renderTerm(slug);
            return;
        }

        renderDictionary();
    }

    function renderDictionary() {

        if (state.currentView !== "dictionary") {

            state.currentView = "dictionary";

            app.innerHTML = `
                <section class="search-section">
                    <input
                        id="searchInput"
                        class="search-input"
                        type="search"
                        placeholder="Szukaj pojęcia..."
                        autocomplete="off"
                        spellcheck="false"
                        aria-label="Szukaj pojęcia"
                    >

                    <div
                        id="resultsMeta"
                        class="results-meta"
                    ></div>
                </section>

                <div
                    id="resultsContainer"
                    class="cards"
                ></div>
            `;

            const searchInput =
                document.getElementById(
                    "searchInput"
                );

            searchInput.value =
                state.query;

            searchInput.addEventListener(
                "input",
                event => {

                    state.query =
                        event.target.value;

                    renderResults();
                }
            );
        }

        renderResults();
    }

    function renderResults() {

        const resultsContainer =
            document.getElementById(
                "resultsContainer"
            );

        const resultsMeta =
            document.getElementById(
                "resultsMeta"
            );

        if (
            !resultsContainer ||
            !resultsMeta
        ) {
            return;
        }

        const query =
            state.query
                .trim()
                .toLowerCase();

        const results =
            state.terms.filter(term => {

                if (!query) {
                    return true;
                }

                return (
                    term.search &&
                    term.search.includes(query)
                );
            });

        resultsMeta.textContent =
            `Znaleziono: ${results.length}`;

        if (results.length === 0) {

            resultsContainer.innerHTML = `
                <div class="empty">
                    Nie znaleziono żadnych wyników.
                </div>
            `;

            return;
        }

        resultsContainer.innerHTML =
            results
                .map(renderCard)
                .join("");
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
                    ${escapeHtml(
                        term.description || ""
                    )}
                </p>

                <div class="badge">
                    ${escapeHtml(
                        term.category || ""
                    )}
                </div>

            </article>
        `;
    }

    function renderTerm(slug) {

        state.currentView = "term";

        const term =
            state.termsBySlug[slug];

        if (!term) {

            renderNotFound();
            return;
        }

        const relatedSection =
            term.related &&
            term.related.length
                ? `
                <section class="related-section">

                    <h2>
                        Powiązane pojęcia
                    </h2>

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

                <a
                    href="#/"
                    class="back-link"
                >
                    ← Powrót do słownika
                </a>

                <header class="article-header">

                    <h1>
                        ${escapeHtml(term.title)}
                    </h1>

                    <div class="badge">
                        ${escapeHtml(
                            term.category || ""
                        )}
                    </div>

                </header>

                <section
                    class="article-content"
                >
                    ${term.content || ""}
                </section>

                ${relatedSection}

            </article>
        `;
    }

    function renderError(message) {

        state.currentView = "error";

        app.innerHTML = `
            <div class="error">

                <h2>
                    Błąd
                </h2>

                <p>
                    ${escapeHtml(message)}
                </p>

            </div>
        `;
    }

    function renderNotFound() {

        state.currentView = "notfound";

        app.innerHTML = `
            <div class="error">

                <h2>
                    Nie znaleziono wpisu
                </h2>

                <p>
                    Podane pojęcie nie istnieje.
                </p>

                <a href="#/">
                    Wróć do słownika
                </a>

            </div>
        `;
    }

    function handleGlobalClick(event) {

        const card =
            event.target.closest(".card");

        if (!card) {
            return;
        }

        const slug =
            card.dataset.slug;

        if (!slug) {
            return;
        }

        location.hash =
            `#/term/${slug}`;
    }

    function escapeHtml(value) {

        const div =
            document.createElement("div");

        div.textContent =
            value ?? "";

        return div.innerHTML;
    }

    initialize();

})();
