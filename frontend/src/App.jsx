import { useState } from "react";

import Dashboard from "./components/Dashboard.jsx";
import Login from "./components/Login.jsx";
import Register from "./components/Register.jsx";

function App() {
  const [token, setToken] = useState(
    localStorage.getItem("token")
  );

  const [showRegister, setShowRegister] = useState(false);

  if (token) {
    return (
      <Dashboard
        token={token}
        onLogout={() => {
          localStorage.removeItem("token");
          setToken(null);
        }}
      />
    );
  }

  if (showRegister) {
    return (
      <Register
        onRegistered={() => {
          setShowRegister(false);
        }}
        onShowLogin={() => {
          setShowRegister(false);
        }}
      />
    );
  }

  return (
    <Login
      onLogin={(newToken) => {
        localStorage.setItem("token", newToken);
        setToken(newToken);
      }}
      onShowRegister={() => {
        setShowRegister(true);
      }}
    />
  );
}

export default App;