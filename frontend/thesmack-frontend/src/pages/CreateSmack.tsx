import React from "react";

// This is the simplified form UI that will go into the Profile page.
const CreateSmack: React.FC = () => {
  // In a real app, this would be a full form with state management and API calls.
  return (
    <div className="create-smack-form">
      <h3>Post a New Smack</h3>
      <textarea
        placeholder="What's on your mind, Massimo?"
        rows={3}
        className="smack-textarea"
      />
      <div className="smack-controls">
        <select className="feeling-select">
          <option value="1">Happy</option>
          <option value="2">Focused</option>
          <option value="3">Anxious</option>
        </select>
        <button className="smack-button">Post</button>
      </div>
    </div>
  );
};

export default CreateSmack;
