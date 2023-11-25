function showDComboBoxes() {
    // Get the value of the third combo box
    var D_Select = document.getElementById("D_Filter");
    var dimensionscombo = document.getElementById("dimensionscombo");
    var D_Value = document.getElementById("D_value");
    var D_Value1 = document.getElementById("D_value1");
    var D_Value2 = document.getElementById("D_value2");
    var D_Filter_type = document.getElementById("D_Filter_type");
    var STRING_FILTER = document.getElementById("DSTR_MatchType");
    var NUMERIC_FILTER = document.getElementById("DNUM_MatchType");
    
    if (D_Select.checked) {
        dimensionscombo.style.display = "block";
        D_Value.style.display = "block";
        D_Filter_type.style.display = "block";
        D_Value1.style.display = "none";
        D_Value2.style.display = "none";
        
    }else{
        dimensionscombo.style.display = "none";
        D_Value.style.display = "none";
        D_Filter_type.style.display = "none";
        D_Value1.style.display = "none";
        D_Value2.style.display = "none";
        STRING_FILTER.style.display= "none";
        NUMERIC_FILTER.style.display= "none";
    }
    
}
function showMComboBoxes() {
    // Get the value of the third combo box
    var M_Select = document.getElementById("M_Filter");
    var metricscombo = document.getElementById("metricscombo");
    var M_Value = document.getElementById("M_value");
    var M_Value1 = document.getElementById("M_value1");
    var M_Value2 = document.getElementById("M_value2");
    var M_Filter_type = document.getElementById("M_Filter_type");
    var STRING_FILTER = document.getElementById("MSTR_MatchType");
    var NUMERIC_FILTER = document.getElementById("MNUM_MatchType");

    if (M_Select.checked) {
        metricscombo.style.display = "block";
        M_Value.style.display = "block";
        M_Filter_type.style.display = "block";
        M_Value1.style.display = "none";
        M_Value2.style.display = "none";
        
    }else{
        metricscombo.style.display = "none";
        M_Value.style.display = "none";
        M_Filter_type.style.display = "none";
        M_Value1.style.display = "none";
        M_Value2.style.display = "none";
        STRING_FILTER.style.display= "none";
        NUMERIC_FILTER.style.display= "none";
    }
    
}

function showDFTComboBoxes() {
    // Get the value of the third combo box
    var valueSelect = document.getElementById("D_Filter_type");
    var selectedOption = valueSelect.options[valueSelect.selectedIndex].value;
    var STRING_FILTER = document.getElementById("DSTR_MatchType");
    var NUMERIC_FILTER = document.getElementById("DNUM_MatchType");
    var Value1 = document.getElementById("D_value1");
    var Value2 = document.getElementById("D_value2");
    var Value = document.getElementById("D_value");

    
    // Show the appropriate combo box based on the selected option
    if (selectedOption === "STRING_FILTER") {
        STRING_FILTER.style.display = "block";
        NUMERIC_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
    } else if (selectedOption === "NUMERIC_FILTER") {
        NUMERIC_FILTER.style.display = "block";
        STRING_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
    }
    else if (selectedOption === "IN_LIST_FILTER") {
        NUMERIC_FILTER.style.display = "none";
        STRING_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
        
    }
    else if (selectedOption === "BETWEEN_FILTER") {
        NUMERIC_FILTER.style.display = "none";
        STRING_FILTER.style.display = "none";
        Value.style.display = "none";
        Value1.style.display = "block";
        Value2.style.display = "block";

    }
}

function showMFTComboBoxes() {
    // Get the value of the third combo box
    var valueSelect = document.getElementById("M_Filter_type");
    var selectedOption = valueSelect.options[valueSelect.selectedIndex].value;

    // Get references to the first and second combo boxes
    var STRING_FILTER = document.getElementById("MSTR_MatchType");
    var NUMERIC_FILTER = document.getElementById("MNUM_MatchType");
    var Value1 = document.getElementById("M_value1");
    var Value2 = document.getElementById("M_value2");
    var Value = document.getElementById("M_value");

    
    // Show the appropriate combo box based on the selected option
    if (selectedOption === "STRING_FILTER") {
        STRING_FILTER.style.display = "block";
        NUMERIC_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
    } else if (selectedOption === "NUMERIC_FILTER") {
        NUMERIC_FILTER.style.display = "block";
        STRING_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
    }
    else if (selectedOption === "IN_LIST_FILTER") {
        NUMERIC_FILTER.style.display = "none";
        STRING_FILTER.style.display = "none";
        Value.style.display = "block";
        Value1.style.display = "none";
        Value2.style.display = "none";
        
    }
    else if (selectedOption === "BETWEEN_FILTER") {
        NUMERIC_FILTER.style.display = "none";
        STRING_FILTER.style.display = "none";
        Value.style.display = "none";
        Value1.style.display = "block";
        Value2.style.display = "block";

    }
}

function filterDimensions() {
    const searchBox = document.querySelector('.search-box.dimensions');
    const checkboxes = document.querySelectorAll('.checkbox-list.dimensions .checkbox-item');

    checkboxes.forEach(checkbox => {
        const label = checkbox.querySelector('.checkbox-label');
        const value = label.textContent.toLowerCase();
        const searchTerm = searchBox.value.toLowerCase();

        if (value.includes(searchTerm)) {
            checkbox.style.display = 'flex'; // Show the checkbox
        } else {
            checkbox.style.display = 'none'; // Hide the checkbox
        }
    });
}

function filterMetrics() {
    const searchBox = document.querySelector('.search-box.metrics');
    const checkboxes = document.querySelectorAll('.checkbox-list.metrics .checkbox-item');

    checkboxes.forEach(checkbox => {
        const label = checkbox.querySelector('.checkbox-label');
        const value = label.textContent.toLowerCase();
        const searchTerm = searchBox.value.toLowerCase();

        if (value.includes(searchTerm)) {
            checkbox.style.display = 'flex'; // Show the checkbox
        } else {
            checkbox.style.display = 'none'; // Hide the checkbox
        }
    });
}

function updateSelectedDimensions() {
    const selectedDimensions = document.getElementById('selected-dimensions');
    selectedDimensions.innerHTML = '';

    const checkboxes = document.querySelectorAll('.checkbox-list.dimensions .checkbox-item input:checked');

    checkboxes.forEach(checkbox => {
        const value = checkbox.value;
        const listItem = document.createElement('li');
        listItem.textContent = value;
        selectedDimensions.appendChild(listItem);
    });
}

function updateSelectedMetrics() {
    const selectedMetrics = document.getElementById('selected-metrics');
    selectedMetrics.innerHTML = '';

    const checkboxes = document.querySelectorAll('.checkbox-list.metrics .checkbox-item input:checked');

    checkboxes.forEach(checkbox => {
        const value = checkbox.value;
        const listItem = document.createElement('li');
        listItem.textContent = value;
        selectedMetrics.appendChild(listItem);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const spinnerContainer = document.getElementById("spinnerContainer");

    function showSpinner() {
        document.querySelector('.spinner-container').style.display = 'flex';
    }
    
    function hideSpinner() {
        document.querySelector('.spinner-container').style.display = 'none';
    }

    const opts = {
        lines: 12,
        length: 10,
        width: 6,
        radius: 12,
        color: "#007bff",
    };

    // Corrected event listeners for search boxes
    const dimensionsSearchBox = document.querySelector('.search-box.dimensions');
    dimensionsSearchBox.addEventListener('input', filterDimensions);

    const metricsSearchBox = document.querySelector('.search-box.metrics');
    metricsSearchBox.addEventListener('input', filterMetrics);

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        showSpinner();

        const response = await fetch("/fetch_data", {
            method: "POST",
            body: new FormData(form),
        });

        hideSpinner();

        if (response.ok) {
            errorContainer.textContent = "";
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "GA_Data.csv";
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        } else {
            console.error("Error retrieving data.");
        }
    });
});
