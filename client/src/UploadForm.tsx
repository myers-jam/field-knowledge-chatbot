import React, { useState } from 'react';
import axios from 'axios';

const UploadForm: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [status, setStatus] = useState('');

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:8000/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setStatus(res.data.message);
    } catch (error) {
      console.error(error);
      setStatus("Upload failed.");
    }
  };

  return (
    <div className="bg-white p-4 rounded shadow w-full max-w-md">
      <h2 className="text-lg font-semibold mb-2">Upload a PDF</h2>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="mb-2"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Upload
      </button>
      {status && <p className="mt-2 text-sm">{status}</p>}
    </div>
  );
};

export default UploadForm;
