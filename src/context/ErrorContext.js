import React, { createContext, useState } from "react";

export const ErrorContext = createContext();

export default function ErrorProvider({ children }) {
  const [showError, setShowError] = useState(false);
  const [errorTitle, setErrorTitle] = useState(false);
  const [errorSubtitle, setErrorSubtitle] = useState(false);

  return (
    <ErrorContext.Provider
      value={{
        showError,
        setShowError,
        errorTitle,
        setErrorTitle,
        errorSubtitle,
        setErrorSubtitle,
      }}
    >
      {children}
    </ErrorContext.Provider>
  );
}
