document.getElementById("login-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, password })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            
            window.location.href = "/prisoners_dashboard";
        } else {
            document.getElementById("error-message").textContent = data.message;
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("error-message").textContent = "An error occurred. Please try again later.";
    }
});
