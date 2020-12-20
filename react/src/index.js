import React, { useState } from "react";
import Scanner from "./components/Scanner";
import ReactDOM from "react-dom";
import Switch from "./Switch";

import "./index.css";

function sendUPC(opts) {
  console.log('Posting request to API...');
  fetch('/api/queue_message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(opts),
  })
  .then(response => response.json())
  .then(opts => {
    console.log('Success:', opts);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}

global.val = false

function App() {

  const [camera, setCamera] = useState(false);
  const [result, setResult] = useState(null);
  const [value, setValue] = useState(false);


  const onDetected = result => {
    setResult(result);
    sendUPC({'upc': result, 'quantity': global.val ? 1 : -1})
    // mqttPublish(client, {'upc': result, 'quantity': global.val ? 1 : -1})
    console.log({'upc': result, 'quantity': global.val ? 1 : -1})
  };

  // I have no clue how "states" work so this is a hack to track the status of the button
  function hello(val) {
    global.val = val;
  }

  return (
    <div className="App">
      <p>{!camera ? '' : result ? result : "Scanning..."}</p>
      <button className="button" onClick={() => setCamera(!camera)}>
          {camera ? "Stop" : "Start"}
      </button>
      <br />
      <br />
      <Switch
        isOn={value}
        onColor="#EF476F"
        handleToggle={() => setValue(!value)}
        onClick={hello(value)}
      />
      <div className="container">
        {camera && <Scanner onDetected={onDetected} />}
      </div>
    </div>
  );
}


const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
