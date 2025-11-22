// Validación simple de dominio institucional en login principal
async function loginHandler(emailId, passId) {
    const email = document.getElementById(emailId)?.value ?? "";
    const password = document.getElementById(passId)?.value ?? "";
    if (!email.endsWith("@ucatolica.edu.co")) {
        alert("El correo debe ser institucional (@ucatolica.edu.co)");
        return;
    }
    if (password.length < 8) {
        alert("La contraseña debe tener mínimo 8 caracteres.");
        return;
    }
    alert("En el proyecto completo aquí se llamaría a /api/v1/auth/login. Para esta versión académica solo se muestra la interfaz.");
    window.location.href = "/panel";
}

document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            e.preventDefault();
            loginHandler("login-email", "login-password");
        });
    }
    const loginFormPage = document.getElementById("login-form-page");
    if (loginFormPage) {
        loginFormPage.addEventListener("submit", (e) => {
            e.preventDefault();
            loginHandler("login-email-page", "login-password-page");
        });
    }

    const regForm = document.getElementById("register-form");
    if (regForm) {
        regForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const email = document.getElementById("reg-email").value;
            if (!email.endsWith("@ucatolica.edu.co")) {
                alert("El correo debe ser institucional @ucatolica.edu.co");
                return;
            }
            alert("En el proyecto final aquí se enviaría el registro a /api/v1/auth/register. Ahora es solo maqueta visual.");
            window.location.href = "/login";
        });
    }

    // Chat simple
    const emotionButtons = document.querySelectorAll(".emotion-btn");
    const chatArea = document.getElementById("chat-area");
    const chatInput = document.getElementById("chat-input");
    const chatSend = document.getElementById("chat-send");

    emotionButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const emotion = btn.dataset.emotion;
            const messages = {
                muy_mal: "Gracias por contarme que te sientes muy mal. Te propongo hacer un ejercicio de respiración para bajar un poco la intensidad de la emoción.",
                triste: "Entiendo que te sientas triste. A veces hablar de lo que nos pasa ayuda a ordenar las ideas.",
                neutral: "Estar neutral también es una emoción válida. Podemos explorar qué ha pasado en tu día.",
                bien: "¡Qué bueno que te sientas bien! Podemos pensar en estrategias para mantener ese bienestar.",
                muy_bien: "Me alegra mucho que te sientas muy bien. Aprovechemos para reforzar tus recursos personales."
            };
            if (chatArea) {
                chatArea.value += "\n\n[Serena] " + messages[emotion];
            }
        });
    });

    if (chatSend && chatArea && chatInput) {
        chatSend.addEventListener("click", () => {
            const text = chatInput.value.trim();
            if (!text) return;
            chatArea.value += "\n\n[Tú] " + text;
            chatArea.value += "\n[Serena] Gracias por compartirlo. Recuerda hacer una pausa, respirar profundo y, si lo necesitas, contactar a Bienestar Universitario.";
            chatInput.value = "";
        });
    }
});
