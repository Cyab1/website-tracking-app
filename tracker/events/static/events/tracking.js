// Wrap the entire script in an Immediately Invoked Function Expression (IIFE)
// to avoid polluting the global namespace.
(function () {
  // Define the sendEvent function to send event data to the server.
  function sendEvent(eventType, extraData = {}) {
    // Create a data object containing the event details.
    const data = {
      event_type: eventType, // The type of event (e.g., "page_load", "click").
      timestamp: new Date().toISOString(), // Current timestamp in ISO format.
      url: window.location.href, // The current URL of the page.
      user_agent: navigator.userAgent, // The user agent string of the browser.
      ...extraData, // Merge any additional data passed to the function.
    };

    // Send the event data to the server using a POST request.
    fetch("http://127.0.0.1:8000/api/events/", {
      method: "POST", // Use the POST method to send data.
      headers: { "Content-Type": "application/json" }, // Set the content type to JSON.
      body: JSON.stringify(data), // Convert the data object to a JSON string.
    }).catch((error) => console.error("Tracking Error:", error)); // Log any errors.
  }

  // Make the sendEvent function globally accessible by attaching it to the window object.
  window.sendEvent = sendEvent;

  // Track the page load event.
  window.addEventListener("load", () => {
    // Send a "page_load" event when the page finishes loading.
    sendEvent("page_load");
  });

  // Track click events on elements.
  document.addEventListener("click", (event) => {
    // Send a "click" event with details about the clicked element.
    sendEvent("click", {
      element: event.target.tagName, // The tag name of the clicked element (e.g., "BUTTON").
      element_id: event.target.id || null, // The ID of the clicked element (if available).
    });
  });

  // Track the time spent on the page.
  let startTime = Date.now(); // Record the time when the page is loaded.
  window.addEventListener("beforeunload", () => {
    // Calculate the duration spent on the page.
    const duration = Date.now() - startTime;
    // Send a "time_spent" event with the duration in milliseconds.
    sendEvent("time_spent", { duration });
  });
})();
