import { useState } from "react";
import api from "../services/api";

function Register({ onRegistered, onShowLogin }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleRegister = async (event) => {
    event.preventDefault();

    setError("");
    setSuccess("");

    try {
      await api.post("/auth/register", {
        username,
        email,
        password,
      });

      setSuccess(
        "Account created successfully!"
      );

      setUsername("");
      setEmail("");
      setPassword("");

      setTimeout(() => {
        onRegistered();
      }, 1000);
    } catch (error) {
      const detail =
        error.response?.data?.detail;

      if (Array.isArray(detail)) {
        setError(
          detail
            .map((item) => item.msg)
            .join(", ")
        );
      } else {
        setError(
          detail || "Registration failed"
        );
      }
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
            Build better.
            <br />
            Together.
          </h1>

          <p>
            Create your workspace, invite your
            team and collaborate in real time.
          </p>

          <div className="feature-list">
            <div className="feature-item">
              <span className="feature-check">✓</span>
              Create team workspaces
            </div>

            <div className="feature-item">
              <span className="feature-check">✓</span>
              Organize conversations
            </div>

            <div className="feature-item">
              <span className="feature-check">✓</span>
              Collaborate instantly
            </div>
          </div>
        </div>
      </div>

      <div className="auth-form-side">
        <div className="auth-card">
          <h2>Create your account 🚀</h2>

          <p className="auth-subtitle">
            Join your team and start collaborating.
          </p>

          <form onSubmit={handleRegister}>
            <div className="form-group">
              <label>Username</label>

              <input
                type="text"
                placeholder="Choose username"
                value={username}
                onChange={(event) =>
                  setUsername(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Email</label>

              <input
                type="email"
                placeholder="you@example.com"
                value={email}
                onChange={(event) =>
                  setEmail(event.target.value)
                }
                required
              />
            </div>

            <div className="form-group">
              <label>Password</label>

              <input
                type="password"
                placeholder="Create password"
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
              Create Account →
            </button>
          </form>

          {error && (
            <div className="error">
              {error}
            </div>
          )}

          {success && (
            <div className="success">
              {success}
            </div>
          )}

          <div className="auth-switch">
            Already have an account?{" "}
            <button
              className="link-button"
              onClick={onShowLogin}
            >
              Sign in
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;