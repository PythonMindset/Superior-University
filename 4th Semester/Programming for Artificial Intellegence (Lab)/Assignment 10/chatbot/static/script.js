const form = document.querySelector("form");
const chatBox = document.getElementById("chat-box");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const userInput = form.user_message.value.trim();
    if (!userInput) return;
    const userMessage = document.createElement("p");
    userMessage.classList.add("user");
    userMessage.innerHTML = `<b>You:</b> ${userInput}`;
    chatBox.appendChild(userMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
    form.user_message.value = "";
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });
    const botMessageText = await response.text();
    const botMessage = document.createElement("p");
    botMessage.classList.add("bot");
    botMessage.innerHTML = `<b>Bot:</b> ${botMessageText}`;
    chatBox.appendChild(botMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
});