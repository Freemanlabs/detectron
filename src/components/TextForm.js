import React, { useContext, useRef } from "react";
import { useState } from "react";
import { Button, Card, Col, Container, Form, Row } from "react-bootstrap";
import axios from "axios";
import { ErrorContext } from "../context/ErrorContext";
import { LoaderContext } from "../context/LoaderContext";
import Result from "./Result";
import Error from "./Error";
import Report from "./Report";

const scrollToRef = (ref) => window.scrollTo(0, ref.current.offsetTop);

export default function TextForm() {
  const reportRef = useRef(null);
  const executeScroll = () => scrollToRef(reportRef);

  const [text, setText] = useState("");
  const [percentage, setPercentage] = useState(0);
  const [showResult, setShowResult] = useState(false);
  const {
    showError,
    setShowError,
    setErrorTitle,
    setErrorSubtitle,
  } = useContext(ErrorContext);
  const { showLoader, setShowLoader } = useContext(LoaderContext);

  const handleSubmit = (event) => {
    event.preventDefault();
    setShowLoader(true);
    setErrorTitle("Scanning for plagiarism");
    setErrorSubtitle("Detectron is looking for plagiarism. Please wait");

    axios.post("/api", { text }).then((res) => {
      setShowLoader(false);
      setPercentage(res.data["percentage_of_similarity"]);
      setShowResult(true);
    });
  };

  const handleUpload = (event) => {
    event.preventDefault();
    if (event.target.value.length > 0) {
      const data = new FormData();
      const file = event.target.files[0];
      data.append("file", file);

      axios.post("/api/upload", data).then((res) => {
        if (res.data === 400) {
          setShowError(true);
          setErrorTitle("This file type is not supported.");
          setErrorSubtitle("Supported types are: .docx and .txt");
        }
        setText(res.data.text);
      });
    }
  };

  const resultText = `<mark>The SPIDER_MIDDLEWARES setting is merged with the
  SPIDER_MIDDLEWARES_BASE setting defined in Scrapy (and not meant to be
  overridden) and then sorted by order to get the final sorted list of
  enabled middleware.
</mark>
<mark>So for example, if at mid-semester or much later on you find out that
your proposed scope can’t be achieved by the end of the semester.</mark>`;

  return (
    <>
      <div className="text-form">
        <Container>
          <Row>
            <Col lg="2" />
            <Col lg="8" className="my-5">
              <Result percentage={4} executeScroll={executeScroll} />
              {showResult && (
                <Result percentage={percentage} executeScroll={executeScroll} />
              )}
              <div style={{ position: "relative" }}>
                {(showError && <Error />) || (showLoader && <Error />)}
                <Card className="card">
                  <Card.Body>
                    <Form
                      id="uploadForm"
                      onSubmit={(event) => {
                        handleSubmit(event);
                      }}
                      encType="multipart/form-data"
                    >
                      <Form.Group>
                        <Form.Control
                          className="textarea"
                          name="area"
                          id="area"
                          as="textarea"
                          rows={6}
                          value={text ? text : ""}
                          placeholder="Enter text or upload file to check for plagiarism"
                          onChange={(event) => {
                            setText(event.target.value);
                          }}
                        />
                      </Form.Group>
                      <div className="text-center mt-4">
                        <Button type="submit" className="btn-info">
                          Scan Plagiarism
                        </Button>
                      </div>
                      <label htmlFor="file" className="text-info">
                        <i className="fa fa-upload" /> Upload a file
                      </label>
                      <Form.File
                        id="file"
                        name="file"
                        hidden
                        onChange={(event) => handleUpload(event)}
                      />
                    </Form>
                  </Card.Body>
                </Card>
              </div>

              {/* Report */}
              <Report reportRef={reportRef} resultText={resultText} />
              {showResult && <Report reportRef={reportRef} />}
            </Col>
          </Row>
        </Container>
      </div>
    </>
  );
}
