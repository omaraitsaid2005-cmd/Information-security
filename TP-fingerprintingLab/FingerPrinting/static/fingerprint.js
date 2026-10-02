// ---------- First active feature ----------
const browserLanguage = navigator.language;
console.log("Browser language:", browserLanguage);

// ---------- Collect additional features from different browser objects ----------
function collectActiveFeatures() {
    return {
        // navigator object
        language: navigator.language,
        languages: (navigator.languages || []).join(","),
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        hardwareConcurrency: navigator.hardwareConcurrency,
        deviceMemory: navigator.deviceMemory !== undefined ? navigator.deviceMemory : "not exposed",
        cookieEnabled: navigator.cookieEnabled,
        doNotTrack: navigator.doNotTrack,

        // screen object
        screenResolution: screen.width + "x" + screen.height,
        availableScreen: screen.availWidth + "x" + screen.availHeight,
        colorDepth: screen.colorDepth,

        // window object
        windowSize: window.innerWidth + "x" + window.innerHeight,
        devicePixelRatio: window.devicePixelRatio,

        // Intl object
        timeZone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        locale: Intl.DateTimeFormat().resolvedOptions().locale,

        // Date object
        timezoneOffset: new Date().getTimezoneOffset(),

        // document object
        referrer: document.referrer || "(none)",
        visibilityState: document.visibilityState
    };
}

// ---------- Display the values on the webpage ----------
function displayFeatures(features) {
    const outputElement = document.getElementById("feature-output");
    let html = "<table border='1' cellpadding='5'>";
    for (const name in features) {
        html += "<tr><td><b>" + name + "</b></td><td>" + features[name] + "</td></tr>";
    }
    html += "</table>";
    outputElement.innerHTML = html;
}

// ---------- Send the features to the Flask server ----------
function sendFeatures(features) {
    fetch("/collect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ type: "active-features", features: features })
    })
        .then(response => response.json())
        .then(answer => console.log("Server answer:", answer))
        .catch(error => console.error("Sending failed:", error));
}

const activeFeatures = collectActiveFeatures();
console.log("Active features:", activeFeatures);
displayFeatures(activeFeatures);
sendFeatures(activeFeatures);