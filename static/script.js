// Smooth scroll navigation
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Intersection Observer for fade-in animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -100px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = "1"
      entry.target.style.transform = "translateY(0)"
    }
  })
}, observerOptions)

// Observe all fade-in elements
document.querySelectorAll(".fade-in").forEach((el) => {
  el.style.opacity = "0"
  el.style.transform = "translateY(30px)"
  el.style.transition = "opacity 0.8s ease-out, transform 0.8s ease-out"
  observer.observe(el)
})

// Copy email to clipboard
function copyEmail(email) {
  navigator.clipboard.writeText(email).then(() => {
    alert("Email copied to clipboard!")
  })
}

const cursorDot = document.querySelector(".cursor-dot")
const cursorRing = document.querySelector(".cursor-ring")

let mouseX = 0
let mouseY = 0
let ringX = 0
let ringY = 0

document.addEventListener("mousemove", (e) => {
  mouseX = e.clientX
  mouseY = e.clientY

  // Move dot immediately
  cursorDot.style.left = mouseX - 4 + "px"
  cursorDot.style.top = mouseY - 4 + "px"
})

// Smooth animation for ring with requestAnimationFrame
function animateRing() {
  ringX += (mouseX - ringX) * 0.2
  ringY += (mouseY - ringY) * 0.2

  cursorRing.style.left = ringX - 15 + "px"
  cursorRing.style.top = ringY - 15 + "px"

  requestAnimationFrame(animateRing)
}

animateRing()
