// Unit conversion logic
function convertUnits() {
  let fromUnit = document.getElementById("unit-from").value;
  let toUnit = document.getElementById("unit-to").value;
  let value = parseFloat(document.getElementById("value").value);

  if (isNaN(value)) {
    document.getElementById("result").textContent = "Please enter a valid number.";
    return;
  }

  console.log(`Converting ${value} from unit ${fromUnit} to unit ${toUnit}`); // Debugging log

  let result = 0;

  // Conversion rates object
  const conversionRates = {
    '0': { '1': value * 30.48, '2': value * 0.3048, '3': value * 12, '4': value * 3 }, // Feet
    '1': { '0': value / 30.48, '2': value / 100, '3': value / 2.54, '4': value / 91.44 }, // Centimeters
    '2': { '0': value * 3.28084, '1': value * 100, '3': value * 39.3701, '4': value * 1.09361 }, // Meters
    '3': { '0': value / 12, '1': value * 2.54, '2': value * 0.0254, '4': value * 0.0277777778 }, // Inches
    '4': { '0': value / 3, '1': value * 91.44, '2': value * 0.9144, '3': value * 36 }, // Yards
    '5': { '1': (value * 9 / 5) + 32, '2': value + 273.15 }, // Celsius
    '6': { '1': (value - 32) / 1.8, '2': (value - 32) * 5 / 9 + 273.15 }, // Fahrenheit
    '7': { '1': value - 273.15, '2': (value - 273.15) * 9 / 5 + 32 }, // Kelvin
    '8': { '1': value * 2.20462, '2': value * 1000, '3': value / 1000, '4': value * 35.274 }, // Kilograms
    '9': { '0': value / 2.20462, '1': value * 453.592, '2': value / 2204.62, '3': value * 16 }, // Pounds
    '10': { '0': value / 1000, '1': value / 453.592, '2': value / 1000000, '3': value / 28.3495 }, // Grams
    '11': { '0': value * 1000, '1': value * 1000000, '2': value * 35273.96, '3': value * 2204.62 }, // Tons
    '12': { '0': value / 35.274, '1': value / 28.3495, '2': value / 16, '3': value / 35273.96 } // Ounces
  };

  // Check if the conversion exists and calculate the result
  if (conversionRates[fromUnit] && conversionRates[fromUnit][toUnit] !== undefined) {
    result = conversionRates[fromUnit][toUnit];
    let formattedValue = formatNumber(value);
    let formattedResult = formatNumber(result);
    document.getElementById("result").textContent = `${formattedValue} converted is ${formattedResult}.`;
  } else {
    document.getElementById("result").textContent = "Conversion not available.";
  }
}

// Format number to display correctly
function formatNumber(number) {
  return Number.isInteger(number) ? number : number.toFixed(2);
}

// Dynamically update the unit options for conversion
function updateUnitToOptions() {
  let fromUnit = document.getElementById("unit-from").value;
  let toSelect = document.getElementById("unit-to");
  toSelect.innerHTML = ''; // Clear current options

  const unitOptions = {
    '0': ['1', '2', '3', '4'],
    '1': ['0', '2', '3', '4'],
    '2': ['0', '1', '3', '4'],
    '3': ['0', '1', '2', '4'],
    '4': ['0', '1', '2', '3'],
    '5': ['1', '2'],
    '6': ['1', '2'],
    '7': ['1', '2'],
    '8': ['1', '2', '3', '4'],
    '9': ['0', '1', '2', '3'],
    '10': ['0', '1', '2', '3'],
    '11': ['0', '1', '2', '3'],
    '12': ['0', '1', '2', '3']
  };

  unitOptions[fromUnit].forEach(unit => {
    let option = document.createElement("option");
    option.value = unit;
    option.textContent = getUnitName(unit);
    toSelect.appendChild(option);
  });
}

// Get the name of the unit for display
function getUnitName(unit) {
  const unitNames = {
    '0': 'Feet',
    '1': 'Centimeters',
    '2': 'Meters',
    '3': 'Inches',
    '4': 'Yards',
    '5': 'Celsius',
    '6': 'Fahrenheit',
    '7': 'Kelvin',
    '8': 'Kilograms',
    '9': 'Pounds',
    '10': 'Grams',
    '11': 'Tons',
    '12': 'Ounces'
  };
  return unitNames[unit];
}

// Initialize unit options on page load
document.addEventListener('DOMContentLoaded', function () {
  updateUnitToOptions();
  document.getElementById("convert-btn").addEventListener("click", convertUnits);
  document.getElementById("unit-from").addEventListener("change", updateUnitToOptions);
});
