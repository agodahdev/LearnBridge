// Run this code when the page fully loads
document.addEventListener("DOMContentLoaded", function() {

    // Find all delete buttons on the page
    let deleteButtons = document.querySelectorAll(".delete-course");

    // Add a confirmation message before deleting a course
    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            if (!confirm("Are you sure you want to delete this course?")) {
                event.preventDefault(); // Stop the delete action if user cancels
            }
        });
    });

    // Find success message box
    let successMessage = document.querySelector(".success-message");

    // Hide the success message after 3 seconds
    if (successMessage) {
        setTimeout(() => {
            successMessage.style.display = "none";
        }, 3000);
    }

    // Get all forms on the page
    let forms = document.querySelectorAll("form");

    // Check for empty fields before submitting a form
    forms.forEach(form => {
        form.addEventListener("submit", function(event) {
            let requiredFields = form.querySelectorAll("input[required], textarea[required]");
            let valid = true;

            // Check each required field
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    valid = false;
                    field.style.border = "2px solid red"; // Highlight empty fields in red
                } else {
                    field.style.border = "1px solid #ccc"; // Reset border color if filled
                }
            });

            if (!valid) {
                event.preventDefault(); // Stop form submission if a field is empty
                alert("Please fill in all required fields.");
            }
        });
    });
});