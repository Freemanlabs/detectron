import React, { useContext } from "react";
import { Card } from "react-bootstrap";
import { ErrorContext } from "../context/ErrorContext";
import { LoaderContext } from "../context/LoaderContext";
import Loader from "./Loader";

export default function Error() {
  const { errorTitle, errorSubtitle, showError, setShowError } = useContext(
    ErrorContext
  );

  const { showLoader } = useContext(LoaderContext);

  const handleClose = () => {
    setShowError(!showError);
  };

  return (
    <>
      <div className="error">
        <Card className="card">
          <Card.Body>
            {showError && (
              <i className="fa fa-times close" onClick={handleClose} />
            )}
            <div className="text-center">
              {showLoader ? (
                <Loader />
              ) : (
                <i className="fa fa-exclamation-triangle warning-icon"></i>
              )}

              <div className="title">{errorTitle}</div>
              <div className="subtitle">{errorSubtitle}</div>
            </div>
          </Card.Body>
        </Card>
      </div>
    </>
  );
}
