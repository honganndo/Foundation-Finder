
document.addEventListener("DOMContentLoaded", function () {

    /*  validate search input */
    var searchForm = document.getElementById("search-form");

    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            var searchInput = document.getElementById("search_input");

            // Check if the search input is empty or contains only whitespace
            if (!searchInput.value.trim()) {
                // Prevent the form submission
                event.preventDefault();

                // Clear the search input
                searchInput.value = "";

                // Refocus on the search input field
                searchInput.focus();
                console.log("no input")               
            }
        });
    }

    /* dynamically generate homepage items based on given list of ids */
    var foundationIds = [1, 7, 10];
    var foundationsContainer = document.getElementById("foundations-container");
  
    var foundationsList = document.getElementById("popular-list");

    // Loop through the foundation IDs and dynamically create list items
    if (foundationsList && data) {
        // Loop through the data and dynamically create list items
        foundationIds.forEach(function (id) {
            // Check if the ID exists in the data
            if (data[id]) {
                var columnDiv = document.createElement("div");
                columnDiv.className = "col-12 col-md-4";

                var foundationLink = document.createElement("a");
                foundationLink.href = "/view/" + id;
                foundationLink.className = "foundation-link";

                var foundationName = document.createElement("span");
                foundationName.textContent = data[id]['Name'];
                foundationName.className = "foundation-name"; // New class for styling

                var foundationImage = document.createElement("img");
                foundationImage.src = data[id]['Image']; // Replace 'ImageUrl' with the actual property name in your data
                foundationImage.alt = data[id]['Name']; // Set alt text for accessibility
                foundationImage.className = "foundation-image";

                var foundationPrice = document.createElement("span");
                foundationPrice.textContent = "Price: " + data[id]['Price']; // Replace 'Price' with the actual property name in your data
                foundationPrice.className = "foundation-price"; // New class for styling

                foundationLink.appendChild(foundationName);
                foundationLink.appendChild(foundationImage);                
                foundationLink.appendChild(foundationPrice);

                columnDiv.appendChild(foundationLink);
                foundationsContainer.appendChild(columnDiv);
            }
        });     
    }

    /* formatting for price on item page */
    var priceInput = document.getElementById("price");
        // Format the price on page load
        formatPrice();

        // Add event listener for input changes
        priceInput.addEventListener("input", function () {
            formatPrice();
        });

        // Function to format the price with a dollar sign
        function formatPrice() {
            // Remove any existing dollar sign
            var inputValue = priceInput.value.replace(/\$/g, '');

            // Format the value with a dollar sign
            priceInput.value = "$" + inputValue;
        }  
    
    /* form submission with AJAX for add item */   
    var addForm = document.getElementById("add-form");

    if (addForm) {
        addForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission
            
            // Call the validateForm function
            var isValid = validateForm();
        
            // If form is valid, proceed with form submission
            if (isValid) {
                var formData = new FormData(addForm);

                fetch("/add", {
                    method: "POST",
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById("success-message").innerHTML = "New item successfully created!  ";
                        document.getElementById("success-message").style.display = "block"; 
                        document.getElementById("success-message").classList.add("success-message");
                        
                        addForm.reset(); // Clear form inputs
                        addForm[0].focus(); // Set focus on the first text box

                        // Add a link/button to view the newly created item
                        var successMessage = document.getElementById("success-message");
                        var viewButton = document.createElement("button");
                        viewButton.textContent = "See it here"
                        viewButton.className = "btn btn-outline-success btn-sm";
                        viewButton.onclick = function() {
                            window.location.href = "/view/" + data.new_id; // Redirect to view the newly created item
                        };
                        successMessage.appendChild(viewButton);
                    } else {
                        console.error("Failed to add item.");
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            }
        });
    }
});

/* function to add color options to list in edit form */
function addColorOption() {
        var colorOptionsContainer = document.getElementById('color-options-container');
        
        var inputGroup = document.createElement('div');
        inputGroup.className = 'input-group';
        
        var input = document.createElement('input');
        input.type = 'text';
        input.className = 'form-control';
        input.name = 'color_option[]'; // Use an array to handle multiple values
        input.required = true;

        var buttonGroup = document.createElement('div');
        buttonGroup.className = 'input-group-append';
        
        var removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.className = 'btn btn-danger';
        removeButton.textContent = 'Remove';
        removeButton.onclick = function() { removeColorOption(removeButton); };

        buttonGroup.appendChild(removeButton);
        inputGroup.appendChild(input);
        inputGroup.appendChild(buttonGroup);
        
        colorOptionsContainer.insertBefore(inputGroup, colorOptionsContainer.lastElementChild);
}

/* function to remove color options in list in edit form */
function removeColorOption(button) {
    var colorOptionToRemove = button.parentNode.parentNode;
    colorOptionToRemove.parentNode.removeChild(colorOptionToRemove);
}

/* function to add similar id options to list in edit form */
function addSimilarId() {
        var similarIdsContainer = document.getElementById('similar-ids-container');
        
        var inputGroup = document.createElement('div');
        inputGroup.className = 'input-group';
        
        var input = document.createElement('input');
        input.type = 'text';
        input.className = 'form-control';
        input.name = 'similar_id[]'; // Use an array to handle multiple values
        input.required = true;

        var buttonGroup = document.createElement('div');
        buttonGroup.className = 'input-group-append';
        
        var removeButton = document.createElement('button');
        removeButton.type = 'button';
        removeButton.className = 'btn btn-danger';
        removeButton.textContent = 'Remove';
        removeButton.onclick = function() { removeSimilarId(removeButton); };

        buttonGroup.appendChild(removeButton);
        inputGroup.appendChild(input);
        inputGroup.appendChild(buttonGroup);
        
        // Insert the new similar foundation ID before the "Add Similar Foundation ID" button
        similarIdsContainer.insertBefore(inputGroup, similarIdsContainer.lastElementChild);
}

/* function to remove similar ids in list in edit form */
function removeSimilarId(button) {
        var similarIdToRemove = button.parentNode.parentNode;
        similarIdToRemove.parentNode.removeChild(similarIdToRemove);
    }

/* ask user if sure and take user back to view item page if discarding changes */
function discardChanges() {
        if (confirm("Are you sure you want to discard changes?")) {
            var id = document.getElementById('itemId').value;
            window.location.href = '/view/' + id;
        }
}

function Cancel() {
        if (confirm("Are you sure you want stop creating a new item?")) {
            window.location.href = '/';
        }
}

/* validation for textarea form with empty or whitespace field */
function validateForm() {
    console.log("Validating form...");
    var field = "summary";
    
    var value = document.getElementById(field).value;
    if (value === null || value.trim() === "") {
        document.getElementById(field).focus();
        console.log("Invalid field")
        return false;
    }    
    return true;
}
