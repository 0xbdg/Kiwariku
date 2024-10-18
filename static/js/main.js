const menuItem = document.querySelector(".group");
const submenu = document.getElementById("submenu");

let currentIndex = 0;
const intervalTime = 5000;

// Function to update the slide position
function updateSlidePosition() {
  const slidesContainer = document.querySelector(".slides-container");
  if (slidesContainer) {
    slidesContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
    updateIndicators();
  }
}

// Function to update the indicators
function updateIndicators() {
  const indicators = document.querySelectorAll("button");
  indicators.forEach((indicator, index) => {
    indicator.classList.toggle("bg-gray-700", index === currentIndex);
    indicator.classList.toggle("bg-gray-400", index !== currentIndex);
  });
}

// Function to go to a specific slide (to fix the error)
function goToSlide(index) {
  currentIndex = index;
  updateSlidePosition();
}

// Function for automatic slide
function autoSlide() {
  const slidesContainer = document.querySelector(".slides-container");
  if (slidesContainer) {
    currentIndex = (currentIndex + 1) % slidesContainer.children.length;
    updateSlidePosition();
  }
}

// Initialize auto-slide
document.addEventListener("DOMContentLoaded", function () {
  setInterval(autoSlide, intervalTime);
  updateSlidePosition(); // Call this function initially to set up the initial state
});

document.addEventListener("DOMContentLoaded", function () {
  // Ambil semua elemen menu yang memiliki submenu
  const menuItems = document.querySelectorAll(".submenu-toggle");
  
  menuItems.forEach((menuItem) => {
      const submenu = menuItem.nextElementSibling; // Get the submenu associated with this menu item

      // Toggle submenu visibility on click
      menuItem.addEventListener("click", (event) => {
          event.preventDefault(); // Prevent default anchor behavior

          const isVisible = submenu.classList.contains("opacity-100");
          
          // Hide all other submenus
          document.querySelectorAll(".submenu").forEach((sub) => {
              if (sub !== submenu) {
                  sub.classList.remove("opacity-100", "visible");
                  sub.classList.add("opacity-0", "invisible");
              }
          });

          // Toggle visibility for the clicked submenu
          if (isVisible) {
              submenu.classList.remove("opacity-100", "visible");
              submenu.classList.add("opacity-0", "invisible");
          } else {
              submenu.classList.remove("opacity-0", "invisible");
              submenu.classList.add("opacity-100", "visible");
              submenu.style.zIndex = "1000"; // Set higher z-index when visible
          }
      });

      // Keep submenu open if mouse is over it
      submenu.addEventListener("mouseenter", () => {
          submenu.classList.remove("opacity-0", "invisible");
          submenu.classList.add("opacity-100", "visible");
          submenu.style.zIndex = "1000"; // Set higher z-index when visible
      });

      // Hide submenu when mouse leaves both menu and submenu
      menuItem.addEventListener("mouseleave", () => {
          setTimeout(() => {
              if (!submenu.matches(":hover")) {
                  submenu.classList.remove("opacity-100", "visible");
                  submenu.classList.add("opacity-0", "invisible");
                  submenu.style.zIndex = "1"; // Reset z-index when hidden
              }
          }, 200);
      });

      submenu.addEventListener("mouseleave", () => {
          setTimeout(() => {
              if (!menuItem.matches(":hover")) {
                  submenu.classList.remove("opacity-100", "visible");
                  submenu.classList.add("opacity-0", "invisible");
                  submenu.style.zIndex = "1"; // Reset z-index when hidden
              }
          }, 200);
      });
  });
});

function Menu(e) {
  let list = document.getElementById("tttttt");
  e.name === "menu"
    ? ((e.name = "close"),
    list.classList.remove("top-[-400px]"),
      list.classList.add("top-[42px]"),
      list.classList.add("opacity-100"),
      list.classList.add("z-[1]"),
      list.classList.remove("opacity-0"))
    : ((e.name = "menu"),
    list.classList.add("top-[-400px]"),
      list.classList.remove("top-[42px]"),
      list.classList.remove("opacity-100"),
      list.classList.remove("z-[1]"),
      list.classList.remove("opacity-0"));
}

document.addEventListener("DOMContentLoaded", function () {
  // Ensure the elements exist
  const inputFile = document.getElementById("input-file");
  const uploadedImage = document.getElementById("uploaded-image");
  const dropArea = document.getElementById("drop-area");

  // Check if all elements are present
  if (!inputFile) {
    console.error("Element with ID 'input-file' not found.");
    return;
  }
  if (!uploadedImage) {
    console.error("Element with ID 'uploaded-image' not found.");
    return;
  }
  if (!dropArea) {
    console.error("Element with ID 'drop-area' not found.");
    return;
  }

  // Event listener for file input changes
  inputFile.addEventListener("change", function (event) {
    const file = event.target.files[0]; // Get the first selected file
    if (file) {
      const reader = new FileReader(); // Create a FileReader object

      // Read the file as a Data URL
      reader.onload = function (e) {
        uploadedImage.src = e.target.result; // Set the image source to the uploaded data
      };

      reader.readAsDataURL(file); // Read the file as a Data URL
    } else {
      console.error("No file uploaded."); // Error handling if no file is selected
    }
  });

  // Handle click on the drop area to open the file selection dialog
  dropArea.onclick = function () {
    inputFile.click();
  };
});