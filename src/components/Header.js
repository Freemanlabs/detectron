import React from "react";
import { Col, Container, Row } from "react-bootstrap";

export default function Header() {
  return (
    <div className="header">
      <div className="py-7 py-lg-8">
        <Container>
          <div className="text-center mb-7 mt-7">
            <Row className="justify-content-center">
              <Col>
                <h1 className="title">Plagiarism Checker by Detectron</h1>
                <div className="subtitle">
                  Detectron’s plagiarism checker detects plagiarism in your
                  text.
                </div>
              </Col>
            </Row>
          </div>
        </Container>
      </div>
    </div>
  );
}
