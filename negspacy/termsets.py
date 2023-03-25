"""
Default termsets for various languages
"""

LANGUAGES = dict()

# english termset dictionary
en = dict()
pseudo = [
    "no further",
    "not able to be",
    "not certain if",
    "not certain whether",
    "not necessarily",
    "without any further",
    "without difficulty",
    "without further",
    "might not",
    "not only",
    "no increase",
    "no significant change",
    "no change",
    "no definite change",
    "not extend",
    "not cause",
]
en["pseudo_negations"] = pseudo

preceding = [
    "absence of",
    "declined",
    "denied",
    "denies",
    "denying",
    "no sign of",
    "no signs of",
    "not",
    "not demonstrate",
    "symptoms atypical",
    "doubt",
    "negative for",
    "no",
    "versus",
    "without",
    "doesn't",
    "doesnt",
    "don't",
    "dont",
    "didn't",
    "didnt",
    "wasn't",
    "wasnt",
    "weren't",
    "werent",
    "isn't",
    "isnt",
    "aren't",
    "arent",
    "cannot",
    "can't",
    "cant",
    "couldn't",
    "couldnt",
    "never",
]
en["preceding_negations"] = preceding

following = [
    "declined",
    "unlikely",
    "was not",
    "were not",
    "wasn't",
    "wasnt",
    "weren't",
    "werent",
]
en["following_negations"] = following

termination = [
    "although",
    "apart from",
    "as there are",
    "aside from",
    "but",
    "except",
    "however",
    "involving",
    "nevertheless",
    "still",
    "though",
    "which",
    "yet",
]
en["termination"] = termination

LANGUAGES["en"] = en

# en_clinical builds upon en
en_clinical = dict()
pseudo_clinical = pseudo + [
    "gram negative",
    "not rule out",
    "not ruled out",
    "not been ruled out",
    "not drain",
    "no suspicious change",
    "no interval change",
    "no significant interval change",
]
en_clinical["pseudo_negations"] = pseudo_clinical

preceding_clinical = preceding + [
    "patient was not",
    "without indication of",
    "without sign of",
    "without signs of",
    "without any reactions or signs of",
    "no complaints of",
    "no evidence of",
    "no cause of",
    "evaluate for",
    "fails to reveal",
    "free of",
    "never developed",
    "never had",
    "did not exhibit",
    "rules out",
    "rule out",
    "rule him out",
    "rule her out",
    "rule patient out",
    "rule the patient out",
    "ruled out",
    "ruled him out",
    "ruled her out",
    "ruled patient out",
    "ruled the patient out",
    "r/o",
    "ro",
]
en_clinical["preceding_negations"] = preceding_clinical

following_clinical = following + ["was ruled out", "were ruled out", "free"]
en_clinical["following_negations"] = following_clinical

termination_clinical = termination + [
    "cause for",
    "cause of",
    "causes for",
    "causes of",
    "etiology for",
    "etiology of",
    "origin for",
    "origin of",
    "origins for",
    "origins of",
    "other possibilities of",
    "reason for",
    "reason of",
    "reasons for",
    "reasons of",
    "secondary to",
    "source for",
    "source of",
    "sources for",
    "sources of",
    "trigger event for",
]
en_clinical["termination"] = termination_clinical
LANGUAGES["en_clinical"] = en_clinical

en_clinical_sensitive = dict()

preceding_clinical_sensitive = preceding_clinical + [
    "concern for",
    "supposed",
    "which causes",
    "leads to",
    "h/o",
    "history of",
    "instead of",
    "if you experience",
    "if you get",
    "teaching the patient",
    "taught the patient",
    "teach the patient",
    "educated the patient",
    "educate the patient",
    "educating the patient",
    "monitored for",
    "monitor for",
    "test for",
    "tested for",
]
en_clinical_sensitive["pseudo_negations"] = pseudo_clinical
en_clinical_sensitive["preceding_negations"] = preceding_clinical_sensitive
en_clinical_sensitive["following_negations"] = following_clinical
en_clinical_sensitive["termination"] = termination_clinical

LANGUAGES["en_clinical_sensitive"] = en_clinical_sensitive


# es_clinical
es_clinical = {
    "pseudo_negations": [
        "sin aumento",
        "ningún cambio",
        "sin cambios sospechosos",
        "ningún cambio significativo",
        "sin cambio de intervalo",
        "sin cambio definitivo",
        "no se extiende",
        "no causa",
        "no drena",
        "cambio de intervalo no significativo",
        "no estoy seguro si",
        "no estoy seguro de si",
        "gram negativo",
        "sin dificultad",
        "no necesariamente",
        "no solo",
        "duda",
        "tengo dudas",
        "dudo",
    ],
    "preceding_negations": [
        "ausencia de",
        "no pueden ver",
        "no poder",
        "revisado para",
        "rechazado",
        "declina",
        "negado",
        "niega",
        "negando",
        "evaluar por",
        "no revela",
        "libre de",
        "negativo para",
        "nunca desarrollado",
        "nunca tuve",
        "no",
        "no anormal",
        "ninguna causa de",
        "sin quejas de",
        "sin evidencia",
        "ninguna nueva evidencia",
        "ninguna otra evidencia",
        "ninguna evidencia para sugerir",
        "sin hallazgos de",
        "no hay hallazgos para indicar",
        "no hay evidencia mamográfica de",
        "nada nuevo",
        "ninguna evidencia radiográfica de",
        "ninguna señal de",
        "no significativo",
        "sin signos de",
        "ninguna sugerencia de",
        "no sospechoso",
        "no",
        "no aparece",
        "no apreciar",
        "no asociado con",
        "no me quejo de",
        "no demostrar",
        "no exhibir",
        "no sentir",
        "no tenía",
        "no tengo",
        "no saber de",
        "no se sabe que tiene",
        "no revelar",
        "no ver",
        "no ser",
        "paciente no era",
        "más bien que",
        "resuelto",
        "hacer una prueba por",
        "excluir",
        "nada especial para",
        "con ningún",
        "sin ninguna evidencia de",
        "sin evidencia",
        "sin indicación de",
        "sin signo de",
        "sin",
        "descartar para",
        "descartarlo por",
        "descartarla por",
        "descartar al paciente por",
        "descartarlo",
        "descartarla",
        "descartar",
        "r / o",
        "ro",
        "descartar al paciente",
        "excluye",
        "lo descarta",
        "la excluye",
        "expulsó al paciente por",
        "gobierna al paciente",
        "lo descartó contra",
        "la descartó contra",
        "lo descartó",
        "la descartó",
        "descartado contra",
        "descartó al paciente contra",
        "descartaron para",
        "descartaron contra",
        "descartó",
        "lo descartaron por",
        "lo descartaron en contra",
        "lo descartaron",
        "la descartaron por",
        "lo descartó contra",
        "lo descartó",
        "descartaron al paciente contra",
        "descartaron al paciente por",
        "descartó al paciente",
        "puede descartar",
        "puede descartar contra",
        "puede descartar",
        "puede descartarlo por",
        "puede descartarlo en contra",
        "puede descartarlo",
        "puede descartarla por",
        "puede descartarla contra",
        "puede descartarla",
        "puede descartar al paciente por",
        "puede descartar al paciente contra",
        "puede descartar al paciente",
        "adecuado para descartar",
        "adecuado para descartar",
        "adecuado para descartarlo por",
        "adecuado para descartarlo",
        "adecuado para descartarla por",
        "adecuado para descartarla",
        "adecuado para descartar al paciente por",
        "adecuado para descartar al paciente contra",
        "adecuado para descartar al paciente",
        "suficiente para descartar",
        "suficiente para descartar",
        "suficiente para descartar",
        "suficiente para descartarlo por",
        "suficiente para descartarlo en contra",
        "suficiente para descartarlo",
        "suficiente para descartarla por",
        "suficiente para descartarla en contra",
        "suficiente para descartarla",
        "suficiente para descartar al paciente por",
        "suficiente para descartar al paciente contra",
        "suficiente para descartar al paciente",
        "lo que debe descartarse es",
    ],
    "following_negations": [
        "debe descartarse para",
        "debe ser descartado para",
        "puede ser descartado para",
        "puede ser descartado para",
        "podría ser descartado por",
        "será descartado por",
        "se puede descartar por",
        "debe descartarse para",
        "debe ser descartado por",
        "ser descartado por",
        "improbable",
        "libre",
        "fue descartado",
        "está descartado",
        "están descartadas",
        "han sido descartadas",
        "ha sido descartado",
        "siendo descartado",
        "debe descartarse",
        "debe ser descartado",
        "puede ser descartado",
        "podría descartarse",
        "podría ser descartado",
        "será descartado",
        "se puede descartar",
        "debe descartarse",
        "debe ser descartado",
        "ser descartado",
        "se descarta",
    ],
    "termination": [
        "pero",
        "sin embargo",
        "sin embargo",
        "todavía",
        "aunque",
        "a pesar de que",
        "todavía",
        "aparte de",
        "excepto",
        "aparte de",
        "secundario a",
        "como la causa de",
        "como fuente de",
        "como la razón de",
        "como la etiología de",
        "como el origen de",
        "como la causa de",
        "como fuente de",
        "como la razón de",
        "como la etiología de",
        "como el origen de",
        "como la causa secundaria de",
        "como la fuente secundaria de",
        "como la razón secundaria de",
        "como la etiología secundaria de",
        "como el origen secundario de",
        "como la causa secundaria de",
        "como la fuente secundaria para",
        "como la razón secundaria para",
        "como la etiología secundaria para",
        "como el origen secundario para",
        "como causa de",
        "como fuente de",
        "como una razón de",
        "como una etiología de",
        "como causa de",
        "como fuente de",
        "como una razón para",
        "como una etiología para",
        "como una causa secundaria de",
        "como una fuente secundaria de",
        "como una razón secundaria de",
        "como una etiología secundaria de",
        "como un origen secundario de",
        "como una causa secundaria para",
        "como una fuente secundaria para",
        "como una razón secundaria para",
        "como una etiología secundaria para",
        "como un origen secundario para",
        "causa de",
        "motivo de",
        "causas de",
        "causas de",
        "fuente de",
        "fuente para",
        "fuentes de",
        "fuentes para",
        "razón de",
        "razón para",
        "razones de",
        "razones para",
        "etiología de",
        "etiología para",
        "desencadenar evento para",
        "origen de",
        "origen para",
        "orígenes de",
        "orígenes para",
        "otras posibilidades de",
    ],
}

LANGUAGES["es_clinical"] = es_clinical


class termset:
    def __init__(self, termset_lang):
        self.pattern_types = [
            "pseudo_negations",
            "preceding_negations",
            "following_negations",
            "termination",
        ]
        self.terms = LANGUAGES[termset_lang]

    def get_patterns(self):
        return self.terms

    def remove_patterns(self, pattern_dict):
        for key, value in pattern_dict.items():
            if key in self.pattern_types:
                self.terms[key] = [i for i in self.terms[key] if i not in value]
            else:
                raise ValueError(f"Unexpected key: {key} not in {self.pattern_types}")

    def add_patterns(self, pattern_dict):
        for key, value in pattern_dict.items():
            if key in self.pattern_types:
                self.terms[key] = list(set(self.terms[key] + value))
            else:
                raise ValueError(f"Unexpected key: {key} not in {self.pattern_types}")
