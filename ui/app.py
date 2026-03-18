"""
ui/app.py
─────────────────────────────────────────────────────────────────
Application TUI — Algèbre & Théorie des Ensembles
Organisée en 5 onglets pédagogiques :

  [Opérations] [Compréhension] [Applications] [Mes Ensembles] [Historique]

Chaque onglet affiche un rappel théorique pour guider l'utilisateur.
"""

from textual.app import App, ComposeResult
from textual.widgets import (
    Button,
    Input,
    Static,
    DataTable,
    Footer,
    Header,
    TabbedContent,
    TabPane,
    Label,
)
from textual.containers import Vertical, Horizontal, ScrollableContainer

from core.operations import (
    union,
    intersection,
    difference,
    symmetric_difference,
    cartesian_product,
    cardinality,
    build_set_by_comprehension,
    build_universe,
    build_function,
    image_directe,
    image_inverse,
    is_injective,
    is_surjective,
    is_bijective,
)
from storage.json_store import (
    load,
    save,
    add_entry,
    get_history,
    clear_history,
    save_named_set,
    load_named_set,
    delete_named_set,
    list_named_sets,
)

# ── Textes théoriques affichés dans chaque onglet ────────────
# Séparés du code pour que tu puisses les modifier facilement
THEORY = {
    "ops": (
        "Rappel  —  Opérations de base\n"
        "  A ∪ B  : union         → éléments dans A OU dans B\n"
        "  A ∩ B  : intersection  → éléments dans A ET dans B\n"
        "  A \\ B  : différence    → éléments dans A mais PAS dans B\n"
        "  A △ B  : diff. sym.    → (A\\B) ∪ (B\\A)\n"
        "  A × B  : produit cart. → toutes les paires (a, b)\n"
        "  |A|    : cardinalité   → nombre d'éléments de A"
    ),
    "comp": (
        "Rappel  —  Ensemble par compréhension\n"
        "  A = { x ∈ E  |  P(x) }\n"
        "  E      : univers (intervalle d'entiers)\n"
        "  P(x)   : prédicat, expression vraie ou fausse\n\n"
        "  Exemples de prédicats :\n"
        "    x % 2 == 0          →  entiers pairs\n"
        "    x > 3 and x < 10   →  ]3 ; 10[\n"
        "    x ** 2 < 50        →  x² < 50"
    ),
    "appli": (
        "Rappel  —  Applications  f : A → B\n"
        "  Injective  : f(x₁) = f(x₂)  ⟹  x₁ = x₂   (pas de collision)\n"
        "  Surjective : ∀ y ∈ B, ∃ x ∈ A tel que f(x) = y  (tout B atteint)\n"
        "  Bijective  : injective ET surjective\n\n"
        "  Image directe  f(S) = { f(x) | x ∈ S }\n"
        "  Image inverse  f⁻¹(T) = { x ∈ A | f(x) ∈ T }"
    ),
}


# ═════════════════════════════════════════════════════════════
#  APPLICATION PRINCIPALE
# ═════════════════════════════════════════════════════════════
class SetApp(App):
    CSS = """
    Screen {
        background: $surface;
    }

    /* ── Boîtes théoriques ── */
    .theory {
        border: dashed $primary-darken-2;
        padding: 1 2;
        margin-bottom: 1;
        color: $text-muted;
    }

    /* ── Champs de saisie ── */
    Input {
        margin: 0 0 1 0;
        border: solid $success-darken-1;
    }

    /* ── Affichage des résultats ── */
    .result {
        border: heavy $warning;
        padding: 1 2;
        color: $warning-lighten-1;
        margin-top: 1;
        min-height: 3;
    }

    /* ── Étiquettes de section ── */
    .section-label {
        color: $accent;
        text-style: bold;
        margin-top: 1;
    }

    /* ── Rangées de boutons ── */
    .btn-row {
        align: center middle;
        height: auto;
        margin: 1 0;
    }

    Button {
        margin: 0 1;
        min-width: 18;
    }

    /* ── Couleurs spéciales ── */
    #btn-quit   { background: $error;   color: $text; }
    #btn-save   { background: $success; color: $text; }
    #btn-delete { background: $error;   color: $text; }

    /* ── Table historique ── */
    DataTable {
        height: 1fr;
        margin-top: 1;
    }

    /* ── Conteneur principal de chaque onglet ── */
    .tab-content {
        padding: 1 2;
        height: 1fr;
    }
    """

    BINDINGS = [
        ("q", "quit_app", "Quitter"),
        ("s", "save_data", "Sauvegarder"),
    ]

    # ── Lifecycle ──────────────────────────────────────────
    def on_mount(self) -> None:
        self.data = load()

    # ── Mise en page ───────────────────────────────────────
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with TabbedContent(initial="tab-ops"):
            # ════════════════════════════════════════
            #  ONGLET 1 — Opérations de base
            # ════════════════════════════════════════
            with TabPane("⊕ Opérations", id="tab-ops"):
                with ScrollableContainer(classes="tab-content"):
                    yield Static(THEORY["ops"], classes="theory")

                    yield Label(
                        "Ensemble A  (entiers séparés par espaces)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 1 2 3 4 5", id="ops-A")

                    yield Label("Ensemble B", classes="section-label")
                    yield Input(placeholder="ex: 3 4 5 6 7", id="ops-B")

                    with Horizontal(classes="btn-row"):
                        yield Button("A ∪ B", id="ops-union")
                        yield Button("A ∩ B", id="ops-inter")
                        yield Button("A \\ B", id="ops-diff")
                        yield Button("A △ B", id="ops-symdiff")

                    with Horizontal(classes="btn-row"):
                        yield Button("A × B", id="ops-prod")
                        yield Button("|A|", id="ops-card")

                    yield Static(
                        "Le résultat apparaîtra ici", id="ops-result", classes="result"
                    )

            # ════════════════════════════════════════
            #  ONGLET 2 — Ensemble par compréhension
            # ════════════════════════════════════════
            with TabPane("∈ Compréhension", id="tab-comp"):
                with ScrollableContainer(classes="tab-content"):
                    yield Static(THEORY["comp"], classes="theory")

                    yield Label("Début de l'univers E", classes="section-label")
                    yield Input(placeholder="ex: -10", id="comp-start")

                    yield Label("Fin de l'univers E", classes="section-label")
                    yield Input(placeholder="ex: 10", id="comp-end")

                    yield Label(
                        "Prédicat P(x)  — expression Python en 'x'",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: x % 2 == 0", id="comp-pred")

                    with Horizontal(classes="btn-row"):
                        yield Button("▶ Construire A", id="comp-build")

                    yield Static(
                        "Le résultat apparaîtra ici", id="comp-result", classes="result"
                    )

            # ════════════════════════════════════════
            #  ONGLET 3 — Applications f : A → B
            # ════════════════════════════════════════
            with TabPane("f(x) Applications", id="tab-appli"):
                with ScrollableContainer(classes="tab-content"):
                    yield Static(THEORY["appli"], classes="theory")

                    yield Label(
                        "① Domaine A  (entiers séparés par espaces)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 1 2 3 4 5", id="f-A")

                    yield Label(
                        "② Codomaine B  (entiers que f(x) peut atteindre)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 1 4 9 16 25", id="f-B")

                    yield Label(
                        "③ Formule de f(x)  — expression Python en 'x'",
                        classes="section-label",
                    )
                    yield Input(
                        placeholder="ex: x ** 2   ou   2*x+1   ou   x % 3",
                        id="f-formula",
                    )

                    yield Label(
                        "④ Sous-ensemble S ⊆ A  pour l'image directe f(S)  (vide = A entier)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 1 2 3", id="f-S")

                    yield Label(
                        "⑤ Sous-ensemble T ⊆ B  pour l'image inverse f⁻¹(T)  (vide = B entier)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 4 9", id="f-T")

                    with Horizontal(classes="btn-row"):
                        yield Button("▶ Analyser f", id="f-analyze")

                    yield Static(
                        "Le résultat apparaîtra ici", id="f-result", classes="result"
                    )

            # ════════════════════════════════════════
            #  ONGLET 4 — Mes Ensembles (sauvegarde)
            # ════════════════════════════════════════
            with TabPane("💾 Mes Ensembles", id="tab-sets"):
                with ScrollableContainer(classes="tab-content"):
                    yield Static(
                        "Sauvegarde nommée  —  donne un nom à tes ensembles\n"
                        "Tu pourras les recharger dans les autres onglets\n"
                        "en écrivant leur nom à la place des chiffres.",
                        classes="theory",
                    )

                    yield Label("Nom de l'ensemble", classes="section-label")
                    yield Input(
                        placeholder="ex: Pairs  ou  MonEnsemble", id="sets-name"
                    )

                    yield Label(
                        "Éléments  (entiers séparés par espaces)",
                        classes="section-label",
                    )
                    yield Input(placeholder="ex: 2 4 6 8 10", id="sets-elements")

                    with Horizontal(classes="btn-row"):
                        yield Button(
                            "💾 Sauvegarder", id="sets-save", variant="success"
                        )
                        yield Button("📂 Charger →  A", id="sets-load-A")
                        yield Button("📂 Charger →  B", id="sets-load-B")
                        yield Button("🗑 Supprimer", id="btn-delete")

                    yield Static("", id="sets-msg", classes="result")

                    yield Label("Ensembles sauvegardés :", classes="section-label")
                    yield DataTable(id="sets-table")

            # ════════════════════════════════════════
            #  ONGLET 5 — Historique
            # ════════════════════════════════════════
            with TabPane("📜 Historique", id="tab-hist"):
                with Vertical(classes="tab-content"):
                    with Horizontal(classes="btn-row"):
                        yield Button("🗑 Effacer l'historique", id="hist-clear")

                    yield DataTable(id="hist-table")

        yield Footer()

    # ── Tables : initialisation au montage ─────────────────
    def on_mount_after(self) -> None:
        """Appelé après compose() — initialise les DataTable."""
        self._init_hist_table()
        self._init_sets_table()

    # Textual déclenche on_mount une seule fois, on initialise ici
    def on_ready(self) -> None:
        self._init_hist_table()
        self._init_sets_table()

    def _init_hist_table(self) -> None:
        t = self.query_one("#hist-table", DataTable)
        if not t.columns:
            t.add_columns("Heure", "Opération", "A", "B", "Résultat")
        self._refresh_hist_table()

    def _refresh_hist_table(self) -> None:
        t = self.query_one("#hist-table", DataTable)
        t.clear()
        history = get_history(self.data)
        if not history:
            t.add_row("—", "Aucun historique", "—", "—", "—")
            return
        for e in reversed(history):
            t.add_row(
                e.get("timestamp", "—"),
                e.get("operation", "—"),
                str(e["operands"].get("A", "—")),
                str(e["operands"].get("B"))
                if e["operands"].get("B") is not None
                else "—",
                str(e.get("result", "—")),
            )

    def _init_sets_table(self) -> None:
        t = self.query_one("#sets-table", DataTable)
        if not t.columns:
            t.add_columns("Nom", "Éléments", "Cardinalité")
        self._refresh_sets_table()

    def _refresh_sets_table(self) -> None:
        t = self.query_one("#sets-table", DataTable)
        t.clear()
        names = list_named_sets(self.data)
        if not names:
            t.add_row("—", "Aucun ensemble sauvegardé", "—")
            return
        for name in names:
            elements = self.data["sets"][name]
            t.add_row(name, str(elements), str(len(elements)))

    # ── Gestion des boutons ────────────────────────────────
    def on_button_pressed(self, event: Button.Pressed) -> None:
        btn = event.button.id

        # ── Actions globales ─────────────────────────
        if btn == "btn-save":
            save(self.data)
            self.notify("Données sauvegardées 💾")
            return

        if btn == "hist-clear":
            clear_history(self.data)
            save(self.data)
            self._refresh_hist_table()
            self.notify("Historique effacé 🗑")
            return

        # ── Onglet Opérations ────────────────────────
        OPS = {
            "ops-union",
            "ops-inter",
            "ops-diff",
            "ops-symdiff",
            "ops-prod",
            "ops-card",
        }
        if btn in OPS:
            self._handle_ops(btn)
            return

        # ── Onglet Compréhension ─────────────────────
        if btn == "comp-build":
            self._handle_comp()
            return

        # ── Onglet Applications ──────────────────────
        if btn == "f-analyze":
            self._handle_appli()
            return

        # ── Onglet Mes Ensembles ─────────────────────
        if btn in {"sets-save", "sets-load-A", "sets-load-B", "btn-delete"}:
            self._handle_sets(btn)
            return

    # ── Logique : Opérations ───────────────────────────────
    def _handle_ops(self, btn: str) -> None:
        result_widget = self.query_one("#ops-result", Static)
        try:
            raw_a = self.query_one("#ops-A", Input).value.strip()
            raw_b = self.query_one("#ops-B", Input).value.strip()

            if not raw_a:
                raise ValueError("L'ensemble A est vide.")

            A = set(map(int, raw_a.split()))
            B = set(map(int, raw_b.split())) if raw_b else set()

            b_used = B
            res = None

            if btn == "ops-union":
                res = union(A, B)
            elif btn == "ops-inter":
                res = intersection(A, B)
            elif btn == "ops-diff":
                res = difference(A, B)
            elif btn == "ops-symdiff":
                res = symmetric_difference(A, B)
            elif btn == "ops-prod":
                res = cartesian_product(A, B)
            elif btn == "ops-card":
                res = cardinality(A)
                b_used = None

            op_name = btn.replace("ops-", "")
            result_widget.update(
                f"A = {sorted(A)}\n"
                f"B = {sorted(B) if b_used is not None else '—'}\n"
                f"Résultat  ({op_name}) : {res}"
            )

            add_entry(self.data, op_name, A, b_used, res)
            self._refresh_hist_table()
            self.notify("✅ Opération réussie")

        except ValueError as e:
            result_widget.update(
                f"⚠️  Saisie invalide : {e}\n(Entrez des entiers séparés par des espaces)"
            )
        except Exception as e:
            result_widget.update(f"⚠️  Erreur : {e}")

    # ── Logique : Compréhension ────────────────────────────
    def _handle_comp(self) -> None:
        result_widget = self.query_one("#comp-result", Static)
        try:
            start = int(self.query_one("#comp-start", Input).value.strip())
            end = int(self.query_one("#comp-end", Input).value.strip())
            pred = self.query_one("#comp-pred", Input).value.strip()

            if start > end:
                raise ValueError("Le début doit être ≤ la fin.")
            if not pred:
                raise ValueError("Le prédicat est vide.")

            E = build_universe(start, end)
            A = build_set_by_comprehension(E, pred)

            result_widget.update(
                f"E = {{ {start}, ..., {end} }}   |E| = {len(E)}\n"
                f"P(x) = « {pred} »\n\n"
                f"A = {sorted(A)}\n"
                f"|A| = {len(A)}"
            )
            self.notify("✅ Ensemble construit")

        except ValueError as e:
            result_widget.update(f"⚠️  Erreur : {e}")
        except Exception as e:
            result_widget.update(f"⚠️  Prédicat invalide : {e}")

    # ── Logique : Applications ─────────────────────────────
    def _handle_appli(self) -> None:
        result_widget = self.query_one("#f-result", Static)
        try:
            A = set(map(int, self.query_one("#f-A", Input).value.split()))
            B = set(map(int, self.query_one("#f-B", Input).value.split()))
            formula = self.query_one("#f-formula", Input).value.strip()
            raw_s = self.query_one("#f-S", Input).value.strip()
            raw_t = self.query_one("#f-T", Input).value.strip()

            if not A:
                raise ValueError("Le domaine A est vide.")
            if not formula:
                raise ValueError("La formule est vide.")

            S = set(map(int, raw_s.split())) if raw_s else A
            T = set(map(int, raw_t.split())) if raw_t else B

            f = build_function(A, formula)

            img_dir = image_directe(f, S)
            img_inv = image_inverse(f, T)
            _, msg_inj = is_injective(f)
            _, msg_sur = is_surjective(f, B)
            _, msg_bij = is_bijective(f, B)

            f_display = "  ".join(f"f({x})={y}" for x, y in sorted(f.items()))

            result_widget.update(
                f"f(x) = {formula}\n"
                f"Valeurs : {f_display}\n\n"
                f"Image directe   f({sorted(S)}) = {sorted(img_dir)}\n"
                f"Image inverse   f⁻¹({sorted(T)}) = {sorted(img_inv)}\n\n"
                f"{msg_inj}\n"
                f"{msg_sur}\n"
                f"{msg_bij}"
            )
            self.notify("✅ Analyse terminée")

        except ValueError as e:
            result_widget.update(f"⚠️  Saisie invalide : {e}")
        except Exception as e:
            result_widget.update(f"⚠️  {e}")

    # ── Logique : Mes Ensembles ────────────────────────────
    def _handle_sets(self, btn: str) -> None:
        msg_widget = self.query_one("#sets-msg", Static)
        name = self.query_one("#sets-name", Input).value.strip()

        if btn == "sets-save":
            try:
                if not name:
                    raise ValueError("Donne un nom à l'ensemble.")
                raw = self.query_one("#sets-elements", Input).value.strip()
                if not raw:
                    raise ValueError("L'ensemble est vide.")
                elements = set(map(int, raw.split()))
                save_named_set(self.data, name, elements)
                save(self.data)
                self._refresh_sets_table()
                msg_widget.update(f"✅  « {name} » = {sorted(elements)}  sauvegardé !")
                self.notify(f"Ensemble '{name}' sauvegardé 💾")
            except ValueError as e:
                msg_widget.update(f"⚠️  {e}")

        elif btn in ("sets-load-A", "sets-load-B"):
            try:
                if not name:
                    raise ValueError("Entre le nom de l'ensemble à charger.")
                elements = load_named_set(self.data, name)
                target_id = "ops-A" if btn == "sets-load-A" else "ops-B"
                # Charger dans le champ A ou B de l'onglet Opérations
                self.query_one(f"#{target_id}", Input).value = " ".join(
                    map(str, sorted(elements))
                )
                target_label = "A" if btn == "sets-load-A" else "B"
                msg_widget.update(
                    f"✅  « {name} » chargé dans le champ {target_label} de l'onglet Opérations."
                )
                self.notify(f"'{name}' → champ {target_label} ✅")
                # Basculer vers l'onglet Opérations
                self.query_one(TabbedContent).active = "tab-ops"
            except KeyError as e:
                msg_widget.update(f"⚠️  {e}")
            except ValueError as e:
                msg_widget.update(f"⚠️  {e}")

        elif btn == "btn-delete":
            try:
                if not name:
                    raise ValueError("Entre le nom de l'ensemble à supprimer.")
                delete_named_set(self.data, name)
                save(self.data)
                self._refresh_sets_table()
                msg_widget.update(f"🗑  « {name} » supprimé.")
                self.notify(f"'{name}' supprimé")
            except ValueError as e:
                msg_widget.update(f"⚠️  {e}")

    # ── Actions clavier ────────────────────────────────────
    def action_quit_app(self) -> None:
        save(self.data)
        self.exit()

    def action_save_data(self) -> None:
        save(self.data)
        self.notify("Données sauvegardées 💾")
