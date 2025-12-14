import React, { useState } from "react";
import { verifyDocument } from "./api";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [extractedText, setExtractedText] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Upload a document first");
      return;
    }
    const res = await verifyDocument(file);
    setResult(res);
    setExtractedText(res.extracted_text || "");
  };

  const handleReset = () => {
    setFile(null);
    setResult(null);
    setExtractedText("");
    document.getElementById("fileInput").value = "";
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    if (droppedFile) setFile(droppedFile);
  };

  return (
    <div className="app-container">
      <h2>Medical Document Verification</h2>

      {/* Drag & Drop Upload */}
      <div
        className="drop-zone"
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
        onClick={() => document.getElementById("fileInput").click()}
      >
        <p>Drag & drop a document here</p>
        <span>or click to browse</span>

        {file && <div className="file-name">{file.name}</div>}
      </div>

      <input
        id="fileInput"
        type="file"
        accept=".pdf,.png,.jpg,.jpeg"
        hidden
        onChange={(e) => setFile(e.target.files[0])}
      />

      <div className="button-group">
        <button className="verify-btn" onClick={handleUpload}>
          Verify
        </button>

        <button className="reset-btn" onClick={handleReset}>
          Reset
        </button>
      </div>

      {/* Verification Result */}
      {result && (
        <div
          className={`result ${
            result.status === "VALID" ? "valid" : "flagged"
          }`}
        >
          <h4>Status: {result.status}</h4>
          <p>{result.message}</p>
        </div>
      )}

      {/* Extracted Text Preview */}
      {extractedText && (
        <div className="text-preview">
          <h4>Extracted Text Preview</h4>
          <pre>{extractedText}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
