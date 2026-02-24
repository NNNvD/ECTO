# Changelog

## [0.2.0](https://github.com/NNNvD/ECTO/compare/v0.1.0...v0.2.0) (2026-02-24)


### Features

* **site:** add logo slot and polished left navigation ([ede1b46](https://github.com/NNNvD/ECTO/commit/ede1b464d53afabcc3e720dd97622cb9b713f3cf))
* **site:** add multi-page docs structure for GitHub Pages ([be45849](https://github.com/NNNvD/ECTO/commit/be45849ac0493d602aac7e6b621ed76c69b77ed1))
* **site:** add multi-page GitHub Pages site (Documents, Logbook, Contact), logo, Quarto/Jekyll config, and workflow fixes ([d4b7784](https://github.com/NNNvD/ECTO/commit/d4b7784a7234f846690fd79725e53952df33d093))
* **site:** add multi-page GitHub Pages site with Documents, Logbook, and Contact ([f449dc2](https://github.com/NNNvD/ECTO/commit/f449dc2606e101d951216bcb4836288a30bc9da4))
* **site:** add root pages nav with documents, logbook, and contact ([30d5361](https://github.com/NNNvD/ECTO/commit/30d53618087f133a373d99f4ff9aba0151288407))
* **site:** add website pages, top-left logo, sidebar TOC and CI adjustments ([76cfe36](https://github.com/NNNvD/ECTO/commit/76cfe361a93529d71faf3c4434569a6310735fb4))
* **site:** limit navigation to requested five pages ([e0752c6](https://github.com/NNNvD/ECTO/commit/e0752c6494ceab2bee52722abc8db969a8c39e6f))
* **site:** restrict Pages nav to Home, Project description, Expert Identification, Search Strategy, and Logbook ([2076321](https://github.com/NNNvD/ECTO/commit/2076321135aa4adeb139b808e59e0cb004a7c154))


### Bug Fixes

* **ci:** configure release-please manifest mode ([2207889](https://github.com/NNNvD/ECTO/commit/2207889f0964f1b51e4eed5ad912db962cf57996))
* **ci:** configure release-please to use manifest config ([4231afb](https://github.com/NNNvD/ECTO/commit/4231afb27e2df5219cc8f09c543e2dcc5287126c))
* **ci:** use include-file blocks and support PAT for release-please ([7e455ba](https://github.com/NNNvD/ECTO/commit/7e455ba921ee361b3fefccf27a200a43ed740689))
* **ci:** use Quarto include-file blocks and add PAT fallback for release-please ([22eab45](https://github.com/NNNvD/ECTO/commit/22eab45af671d0dcd2aa7cbe379d2dda2d27a650))
* correct ADR numbering regex ([cab6ce8](https://github.com/NNNvD/ECTO/commit/cab6ce8c9e470533f8ef6b839d3b876410a4d140))
* **release:** add issues permission and canonical manifest config ([4fb0ada](https://github.com/NNNvD/ECTO/commit/4fb0ada90024dd7facc14ab908ec4df933eac550))
* **release:** align permissions for release-please PR creation ([a7119cc](https://github.com/NNNvD/ECTO/commit/a7119cc2744956aa394fca37b252e95ee6cd7306))
* **release:** align workflow permissions and add manual trigger for release-please ([a631d08](https://github.com/NNNvD/ECTO/commit/a631d0819e3f512d2663f55bc4fbe50be04341f8))
* **release:** correct invalid GitHub Actions expression in release workflow ([6d15fc2](https://github.com/NNNvD/ECTO/commit/6d15fc28e95167039756a07222f8f98292154933))
* **release:** stabilize release-please workflow permissions and manifest config ([f1a6c8a](https://github.com/NNNvD/ECTO/commit/f1a6c8a0e9d1c3cead6460bdcbc329ca92b364aa))
* **release:** use valid token fallback expression ([2d1383f](https://github.com/NNNvD/ECTO/commit/2d1383f5a7d8dbc33c7efa42b32585bb20e0de76))
* **site:** avoid front-matter parse errors in documents page includes ([26ea7fd](https://github.com/NNNvD/ECTO/commit/26ea7fdc928ce20c7b67e927e71c2335d1ebbc31))
* **site:** avoid Quarto YAML parse errors in documents page by using sanitized includes ([138118d](https://github.com/NNNvD/ECTO/commit/138118d0590dab262b9df6623a6ed6ad716ff869))
* **site:** exclude include fragments from Quarto render targets ([e6e87fd](https://github.com/NNNvD/ECTO/commit/e6e87fd3fcccfc3684f73ce531d791bf4d92b777))
* **site:** hide unwanted nav entries and restore contact order ([5397722](https://github.com/NNNvD/ECTO/commit/53977221b1277127d623ac44a2a7a2f7ffab5b5b))
* **site:** hide unwanted sidebar entries and keep requested page order ([ab8ff30](https://github.com/NNNvD/ECTO/commit/ab8ff30f32839fd66345b371c8b77b0a23774128))
* **site:** prevent Quarto from rendering include fragments as pages ([a728ba3](https://github.com/NNNvD/ECTO/commit/a728ba312532a6c4828d9c492a56f39596a78de3))
* **site:** whitelist only requested nav pages and exclude legacy documents route ([cc532b2](https://github.com/NNNvD/ECTO/commit/cc532b2016b0833269c1bcc4d16163ce5faf11e0))
* **site:** whitelist sidebar pages and disable legacy documents page build ([358e877](https://github.com/NNNvD/ECTO/commit/358e877fe693c8234d86405d529a08e26cc4e19e))
