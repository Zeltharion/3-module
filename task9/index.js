const form = document.getElementById("calculator-form")

form.addEventListener("submit", function (event) {
	event.preventDefault()
	const expressionInput = document.getElementById("expression").value.trim()
	const resultElement = document.getElementById("result")

	if (!expressionInput) {
		resultElement.textContent = ""
		return
	}

	try {
		const formattedExpression = expressionInput.replace(/\^/g, "**")
		const result = eval(formattedExpression)
		resultElement.textContent = `Результат: ${result}`
	} catch (error) {
		resultElement.textContent = "Ошибка в выражении. Проверьте корректность ввода."
	}
})
