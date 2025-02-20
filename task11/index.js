const canvas = document.getElementById("drawingCanvas")
const context = canvas.getContext("2d")
canvas.width = canvas.offsetWidth
canvas.height = canvas.offsetHeight

let drawing = false
let currentColor = "#ff0000"

canvas.addEventListener("mousedown", startDrawing)
canvas.addEventListener("mouseup", stopDrawing)
canvas.addEventListener("mousemove", draw)
document.querySelectorAll(".color-button").forEach((button) => {
	button.addEventListener("click", () => {
		currentColor = button.getAttribute("data-color")
	})
})

function startDrawing(e) {
	drawing = true
	draw(e)
}

function stopDrawing() {
	drawing = false
	context.beginPath()
}

function draw(e) {
	if (!drawing) return

	const rect = canvas.getBoundingClientRect()
	const x = e.clientX - rect.left
	const y = e.clientY - rect.top

	context.lineWidth = 5
	context.lineCap = "round"
	context.strokeStyle = currentColor

	context.lineTo(x, y)
	context.stroke()
	context.beginPath()
	context.moveTo(x, y)
}
