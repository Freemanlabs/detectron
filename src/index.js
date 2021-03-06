import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import "./assets/vendor/@fortawesome/fontawesome-free/css/all.min.css";
import "./assets/scss/main.scss";
import ErrorProvider from "./context/ErrorContext";
import LoaderProvider from "./context/LoaderContext";

ReactDOM.render(
  <React.StrictMode>
    <ErrorProvider>
      <LoaderProvider>
        <App />
      </LoaderProvider>
    </ErrorProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
