import React from 'react';
import UploadForm from './UploadForm';
import ChatBox from './ChatBox';

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-2xl font-bold mb-6">Field Knowledge Chatbot</h1>
      <UploadForm />
      <ChatBox />
    </div>
  );
};

export default App;
