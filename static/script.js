function sendMessage() {
    let chatbox = document.getElementById("chatbox");
    let message = chatbox.value;
    chatbox.value = ""; // Clear chatbox after sending

    // Placeholder chatbot response
    alert("You said: " + message + ". Serene AI responds: Stay calm and take a deep breath.");
}
