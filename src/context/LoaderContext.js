import React, { createContext, useState } from "react";

export const LoaderContext = createContext();

export default function LoaderProvider({ children }) {
  const [showLoader, setShowLoader] = useState(false);

  return (
    <LoaderContext.Provider
      value={{
        showLoader,
        setShowLoader,
      }}
    >
      {children}
    </LoaderContext.Provider>
  );
}
