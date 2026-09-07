import streamlit as st
from fractions import Fraction

st.set_page_config(
    page_title="Matemática 7° - Raíz de un Cociente",
    page_icon="📐",
    layout="centered"
)

st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1e3a8a;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        color: #475569;
        font-size: 1.2rem;
        margin-bottom: 1.5rem;
    }
    .step-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📐 Matemática - 7° Grado</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Propiedad de la Radicación: <strong>Raíz de un Cociente</strong></div>', unsafe_allow_html=True)

# 20 ejercicios que incluyen raíces cúbicas de números negativos con resultados lindos
EJERCICIOS = [
    {"index": 2, "num": 1,   "den": 4,   "ans": Fraction(1, 2),   "tex": r"\sqrt{\frac{1}{4}}"},
    {"index": 2, "num": 9,   "den": 16,  "ans": Fraction(3, 4),   "tex": r"\sqrt{\frac{9}{16}}"},
    {"index": 3, "num": 1,   "den": 8,   "ans": Fraction(-1, 2),  "tex": r"\sqrt[3]{-\frac{1}{8}}"},
    {"index": 2, "num": 1,   "den": 9,   "ans": Fraction(1, 3),   "tex": r"\sqrt{\frac{1}{9}}"},
    {"index": 2, "num": 16,  "den": 25,  "ans": Fraction(4, 5),   "tex": r"\sqrt{\frac{16}{25}}"},
    {"index": 3, "num": 8,   "den": 27,  "ans": Fraction(-2, 3),  "tex": r"\sqrt[3]{-\frac{8}{27}}"},
    {"index": 2, "num": 49,  "den": 64,  "ans": Fraction(7, 8),   "tex": r"\sqrt{\frac{49}{64}}"},
    {"index": 2, "num": 4,   "den": 25,  "ans": Fraction(2, 5),   "tex": r"\sqrt{\frac{4}{25}}"},
    {"index": 3, "num": 27,  "den": 64,  "ans": Fraction(-3, 4),  "tex": r"\sqrt[3]{-\frac{27}{64}}"},
    {"index": 2, "num": 81,  "den": 100, "ans": Fraction(9, 10),  "tex": r"\sqrt{\frac{81}{100}}"},
    {"index": 3, "num": 1,   "den": 8,   "ans": Fraction(1, 2),   "tex": r"\sqrt[3]{\frac{1}{8}}"},
    {"index": 3, "num": 8,   "den": 27,  "ans": Fraction(2, 3),   "tex": r"\sqrt[3]{\frac{8}{27}}"},
    {"index": 3, "num": 1,   "den": 125, "ans": Fraction(-1, 5),  "tex": r"\sqrt[3]{-\frac{1}{125}}"},
    {"index": 2, "num": 25,  "den": 49,  "ans": Fraction(5, 7),   "tex": r"\sqrt{\frac{25}{49}}"},
    {"index": 3, "num": 64,  "den": 125, "ans": Fraction(-4, 5),  "tex": r"\sqrt[3]{-\frac{64}{125}}"},
    {"index": 2, "num": 100, "den": 9,   "ans": Fraction(10, 3),  "tex": r"\sqrt{\frac{100}{9}}"},
    {"index": 2, "num": 121, "den": 144, "ans": Fraction(11, 12), "tex": r"\sqrt{\frac{121}{144}}"},
    {"index": 2, "num": 64,  "den": 4,   "ans": Fraction(4, 1),   "tex": r"\sqrt{\frac{64}{4}}"},
    {"index": 2, "num": 1,   "den": 36,  "ans": Fraction(1, 6),   "tex": r"\sqrt{\frac{1}{36}}"},
    {"index": 3, "num": 1,   "den": 27,  "ans": Fraction(-1, 3),  "tex": r"\sqrt[3]{-\frac{1}{27}}"},
]

def parse_respuesta(texto: str):
    texto = texto.strip().replace(" ", "")
    if not texto:
        return None
    try:
        if "/" in texto:
            partes = texto.split("/")
            if len(partes) != 2:
                return None
            n = int(partes[0])
            d = int(partes[1])
            if d == 0:
                return None
            return Fraction(n, d)
        else:
            return Fraction(int(texto), 1)
    except ValueError:
        return None

if "ej_idx" not in st.session_state:
    st.session_state.ej_idx = 0
if "resueltos" not in st.session_state:
    st.session_state.resueltos = set()
if "feedback" not in st.session_state:
    st.session_state.feedback = None

tab1, tab2, tab3 = st.tabs(["📖 1. Explicación Teórica", "💡 2. Tres Ejemplos", "✏️ 3. Práctica (20 Ejercicios)"])

# ----------------- TAB 1: TEORÍA -----------------
with tab1:
    st.header("📖 Propiedad de la Raíz de un Cociente")
    st.write("La propiedad establece que la raíz de una división o fracción se puede calcular distribuyendo el radical:")

    st.latex(r"\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}")

    st.markdown("### Conjuntos numéricos a los que pertenecen:")
    st.markdown("""
    * **$a \in \mathbb{Z}$** $\\rightarrow$ **$a$** pertenece al conjunto de los números **enteros**.
    * **$b \in \mathbb{Z} - \{0\}$** $\\rightarrow$ **$b$** pertenece al conjunto de los números **enteros excluyendo el 0** (no existe la división por cero).
    * **$n \in \mathbb{N}$ ($n \ge 2$)** $\\rightarrow$ **$n$** pertenece al conjunto de los números **naturales** (índice del radical).
    
    *Nota: Si el índice $n$ es par, el radicando debe ser no negativo ($\frac{a}{b} \ge 0$). Si el índice $n$ es impar, el radicando puede ser positivo o negativo.*
    """)

# ----------------- TAB 2: EJEMPLOS -----------------
with tab2:
    st.header("💡 3 Ejemplos Paso a Paso")
    st.write("Observa cómo aplicamos la propiedad en números racionales (ℚ) con resultados exactos y lindos:")

    st.markdown("""
    <div class="step-card">
        <h4 style="color: #1d4ed8; margin-bottom: 0.5rem;">Ejemplo 1: Raíz cuadrada de una fracción</h4>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"\sqrt{\frac{4}{9}} = \frac{\sqrt{4}}{\sqrt{9}} = \frac{2}{3}")
    st.write("1. **Repartimos la raíz:** Raíz de 4 en el numerador y raíz de 9 en el denominador.")
    st.write("2. **Resolvemos arriba:** $\\sqrt{4} = 2$ (porque $2 \\times 2 = 4$).")
    st.write("3. **Resolvemos abajo:** $\\sqrt{9} = 3$ (porque $3 \\times 3 = 9$).")
    st.write("✨ **Resultado:** **2/3** (dos tercios).")

    st.markdown("---")

    st.markdown("""
    <div class="step-card">
        <h4 style="color: #047857; margin-bottom: 0.5rem;">Ejemplo 2: Raíz cúbica de una fracción positiva</h4>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"\sqrt[3]{\frac{8}{27}} = \frac{\sqrt[3]{8}}{\sqrt[3]{27}} = \frac{2}{3}")
    st.write("1. **Repartimos la raíz cúbica:** $\\sqrt[3]{8}$ arriba y $\\sqrt[3]{27}$ abajo.")
    st.write("2. **Resolvemos arriba:** La raíz cúbica de 8 es 2 (porque $2 \\times 2 \\times 2 = 8$).")
    st.write("3. **Resolvemos abajo:** La raíz cúbica de 27 es 3 (porque $3 \\times 3 \\times 3 = 27$).")
    st.write("✨ **Resultado:** **2/3** (dos tercios).")

    st.markdown("---")

    # Ejemplo 3: Raíz cúbica y negativa
    st.markdown("""
    <div class="step-card">
        <h4 style="color: #b91c1c; margin-bottom: 0.5rem;">Ejemplo 3: Raíz cúbica de una fracción negativa</h4>
    </div>
    """, unsafe_allow_html=True)
    st.latex(r"\sqrt[3]{-\frac{8}{27}} = \frac{\sqrt[3]{-8}}{\sqrt[3]{27}} = \frac{-2}{3} = -\frac{2}{3}")
    st.write("1. **Repartimos la raíz cúbica:** $\\sqrt[3]{-8}$ en el numerador y $\\sqrt[3]{27}$ en el denominador.")
    st.write("2. **Resolvemos el numerador:** $\\sqrt[3]{-8} = -2$ (porque $(-2) \\times (-2) \\times (-2) = -8$).")
    st.write("3. **Resolvemos el denominador:** $\\sqrt[3]{27} = 3$ (porque $3 \\times 3 \\times 3 = 27$).")
    st.write("✨ **Resultado:** **-2/3** (menos dos tercios).")

# ----------------- TAB 3: EJERCICIOS -----------------
with tab3:
    total_ej = len(EJERCICIOS)
    cant_resueltos = len(st.session_state.resueltos)

    col_prog1, col_prog2 = st.columns([3, 1])
    with col_prog1:
        st.progress(cant_resueltos / total_ej)
    with col_prog2:
        st.write(f"**Resueltos:** {cant_resueltos} / {total_ej}")

    opciones_ej = [f"Ejercicio {i+1} {'✅' if i in st.session_state.resueltos else ''}" for i in range(total_ej)]
    sel_idx = st.selectbox(
        "Seleccionar ejercicio:",
        range(total_ej),
        index=st.session_state.ej_idx,
        format_func=lambda x: opciones_ej[x]
    )

    if sel_idx != st.session_state.ej_idx:
        st.session_state.ej_idx = sel_idx
        st.session_state.feedback = None
        st.rerun()

    current = EJERCICIOS[st.session_state.ej_idx]

    st.markdown(f"### Ejercicio {st.session_state.ej_idx + 1} de {total_ej}")
    st.markdown("Calcula aplicando la propiedad:")
    st.latex(current["tex"] + " = ?")

    with st.form(key=f"form_ej_{st.session_state.ej_idx}"):
        resp_input = st.text_input(
            "Escribe tu respuesta:",
            placeholder="ej: -2/3 o 4",
            help="Escribe como fracción (ejemplo: 3/4 o -2/3) o entero (ejemplo: 4 o -2)."
        )
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            submit = st.form_submit_button("🔍 Verificar", use_container_width=True)

        if submit:
            parsed = parse_respuesta(resp_input)
            if parsed is None:
                st.session_state.feedback = "invalid"
            elif parsed == current["ans"]:
                st.session_state.feedback = "ok"
                st.session_state.resueltos.add(st.session_state.ej_idx)
            else:
                st.session_state.feedback = "error"

    if st.session_state.feedback == "ok":
        st.success("🎉 ¡Está bien! ¡Excelente trabajo!")
        if len(st.session_state.resueltos) == total_ej:
            st.balloons()
            st.info("🏆 ¡Felicitaciones! Has completado los 20 ejercicios.")
        else:
            if st.button("➡️ Siguiente Ejercicio", use_container_width=True):
                st.session_state.ej_idx = (st.session_state.ej_idx + 1) % total_ej
                st.session_state.feedback = None
                st.rerun()
    elif st.session_state.feedback == "error":
        st.error("❌ Está mal. ¡Intenta otra vez! Revisa tus cuentas.")
    elif st.session_state.feedback == "invalid":
        st.warning("⚠️ Formato no válido. Escribe una fracción como `3/4` o `-2/3`, o un entero como `4`.")
