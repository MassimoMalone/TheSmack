import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // This runs once when the component mounts
    fetch("http://127.0.0.1:8000/api/hello") // your backend URL
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <nav>{/* You can include your Navbar component here */}</nav>
      <main>
        <h1>Welcome to The Smack!</h1>
        <p>Backend says: {message}</p>
      </main>
    </div>
  );
}

export default App;
