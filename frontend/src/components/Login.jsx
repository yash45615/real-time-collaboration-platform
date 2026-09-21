import { useState } from "react";
import api from "../services/api";

function Login({ onLogin, onShowRegister }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (event) => {
    event.preventDefault();
    setError("");

    try {
      const response = await api.post("/auth/login", {
        username,
        password,
      });

      onLogin(response.data.access_token);
    } catch (error) {
      setError(
        error.response?.data?.detail ||
          "Login failed"
      );
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-visual">
        <div className="visual-content">
          <div className="logo-large">
            <div className="logo-icon">⚡</div>
            <div className="logo-text">
              CollabSpace
            </div>
          </div>

          <h1>
            Work together.
            <br />
            In real time.
          </h1>

          <p>
            Connect your team, organize workspaces,
            communicate through channels and
            collaborate in real time.
          </p>

          <div className="feature-list">
            <div className="feature-item">
              <span className="feature-check">✓</span>
              Real-time communication
            </div>

            <div className="feature-item">
              <span className="feature-check">✓</span>
              Team workspaces
            </div>

            <div className="feature-item">
              <span className="feature-check">✓</span>
              Secure authentication
            </div>
          </div>
        </div>
      </div>

      <div className="auth-form-side">
        <div className="auth-card">
          <h2>Welcome back 👋</h2>

          <p className="auth-subtitle">
            Sign in to continue to your workspace.
          </p>

          <form onSubmit={handleLogin}>
            <div className="form-group">
              <label>Username</label>

              <input
                type="text"
                placeholder="Enter username"
                value={username}
                onChange={(event) =>
                  setUsername(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Password</label>

              <input
                type="password"
                placeholder="Enter password"
                value={password}
                onChange={(event) =>
                  setPassword(event.target.value)
                }
                required
              />
            </div>

            <button
              className="primary-button"
              type="submit"
            >
              Sign In →
            </button>
          </form>

          {error && (
            <div className="error">
              {error}
            </div>
          )}

          <div className="auth-switch">
            Don't have an account?{" "}
            <button
              className="link-button"
              onClick={onShowRegister}
            >
              Create one
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;