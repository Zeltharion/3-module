document.addEventListener("DOMContentLoaded", function () {
	const redSlider = document.getElementById("red")
	const greenSlider = document.getElementById("green")
	const blueSlider = document.getElementById("blue")

	const redValue = document.getElementById("redValue")
	const greenValue = document.getElementById("greenValue")
	const blueValue = document.getElementById("blueValue")

	const colorDisplay = document.getElementById("colorDisplay")
	const rgbCode = document.getElementById("rgbCode")

	function updateColor() {
		const red = redSlider.value
		const green = greenSlider.value
		const blue = blueSlider.value

		const rgb = `rgb(${red}, ${green}, ${blue})`

		redValue.textContent = red
		greenValue.textContent = green
		blueValue.textContent = blue

		colorDisplay.style.backgroundColor = rgb
		rgbCode.textContent = rgb
	}

	redSlider.addEventListener("input", updateColor)
	greenSlider.addEventListener("input", updateColor)
	blueSlider.addEventListener("input", updateColor)

	updateColor()
})
