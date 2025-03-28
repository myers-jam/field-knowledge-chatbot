import React, { useState } from 'react';
import axios from 'axios';

const ChatBox: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSend = async () => {
    if (!question.trim()) return;

    try {
      const res = await axios.post("http://localhost:8000/query/", { question });
      setAnswer(res.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong.");
    }
  };

  return (
    <div className="bg-white p-4 rounded shadow w-full max-w-md mt-4">
      <h2 className="text-lg font-semibold mb-2">Ask a Question</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Type your question..."
        className="w-full border p-2 rounded mb-2"
      />
      <button
        onClick={handleSend}
        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
      >
        Send
      </button>
      {answer && <p className="mt-4 whitespace-pre-wrap">{answer}</p>}
    </div>
  );
};

export default ChatBox;
