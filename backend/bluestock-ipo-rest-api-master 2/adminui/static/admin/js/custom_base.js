function toggleDropdown() {
    var content = document.getElementById("dropdown-content");
    var arrowIcon = document.querySelector("#dropdown .arrow i");
  
    if (content.classList.contains("hidden")) {
      content.classList.remove("hidden");
      content.classList.add("visible");
      arrowIcon.classList.remove("fa-angle-down");
      arrowIcon.classList.add("fa-angle-up");
    } else {
      content.classList.remove("visible");
      content.classList.add("hidden");
      arrowIcon.classList.remove("fa-angle-up");
      arrowIcon.classList.add("fa-angle-down");
    }
  }
  
  function toggleDropdown1() {
    var content = document.getElementById("dropdown-content1");

    if (content.classList.contains("hidden")) {
        content.classList.remove("hidden");
        content.classList.add("visible");
    } else {
        content.classList.remove("visible");
        content.classList.add("hidden");
    }
}
