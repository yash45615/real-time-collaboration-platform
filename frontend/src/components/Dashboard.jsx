import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard({ token, onLogout }) {
  const [profile, setProfile] = useState(null);
  const [workspaces, setWorkspaces] = useState([]);

  const [workspaceName, setWorkspaceName] =
    useState("");

  const [workspaceDescription, setWorkspaceDescription] =
    useState("");

  const loadDashboard = async () => {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      const profileResponse = await api.get(
        "/users/me",
        { headers }
      );

      setProfile(profileResponse.data);

      const workspaceResponse = await api.get(
        "/workspaces",
        { headers }
      );

      setWorkspaces(workspaceResponse.data);
    } catch (error) {
      console.error(
        "Dashboard error:",
        error
      );
    }
  };

  useEffect(() => {
    loadDashboard();
  }, []);

  const createWorkspace = async (event) => {
    event.preventDefault();

    if (!workspaceName.trim()) {
      return;
    }

    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };

      await api.post(
        "/workspaces",
        {
          name: workspaceName,
          description: workspaceDescription,
        },
        { headers }
      );

      setWorkspaceName("");
      setWorkspaceDescription("");

      loadDashboard();
    } catch (error) {
      console.error(
        "Create workspace error:",
        error
      );
    }
  };

  const username =
    profile?.username || "User";

  return (
    <div className="dashboard-layout">

      <aside className="sidebar">

        <div className="sidebar-logo">
          <div className="sidebar-logo-icon">
            ⚡
          </div>

          <span>CollabSpace</span>
        </div>

        <div className="sidebar-section">

          <div className="sidebar-label">
            MAIN
          </div>

          <button className="sidebar-item active">
            🏠 Dashboard
          </button>

          <button className="sidebar-item">
            💬 Channels
          </button>

          <button className="sidebar-item">
            👥 Members
          </button>

          <button className="sidebar-item">
            🔔 Notifications
          </button>

        </div>

        <div className="sidebar-section">

          <div className="sidebar-label">
            SYSTEM
          </div>

          <button className="sidebar-item">
            ⚙️ Settings
          </button>

        </div>

      </aside>

      <main className="main-content">

        <div className="topbar">

          <div>
            <h1>Dashboard</h1>

            <p>
              Manage your collaboration spaces
            </p>
          </div>

          <div className="user-area">

            <div className="avatar">
              {username
                .charAt(0)
                .toUpperCase()}
            </div>

            <button
              className="logout-button"
              onClick={onLogout}
            >
              Logout
            </button>

          </div>

        </div>

        <div className="hero-card">

          <h2>
            Welcome back, {username} 👋
          </h2>

          <p>
            Create a workspace and start
            collaborating with your team.
          </p>

        </div>

        <div className="dashboard-grid">

          <section className="panel">

            <div className="panel-header">
              <h2>Create Workspace</h2>
            </div>

            <form
              className="workspace-form"
              onSubmit={createWorkspace}
            >

              <input
                type="text"
                placeholder="Workspace name"
                value={workspaceName}
                onChange={(event) =>
                  setWorkspaceName(
                    event.target.value
                  )
                }
                required
              />

              <input
                type="text"
                placeholder="Description"
                value={workspaceDescription}
                onChange={(event) =>
                  setWorkspaceDescription(
                    event.target.value
                  )
                }
              />

              <button
                className="primary-button"
                type="submit"
              >
                + Create Workspace
              </button>

            </form>

          </section>

          <section className="panel">

            <div className="panel-header">

              <h2>Your Workspaces</h2>

              <span>
                {workspaces.length} total
              </span>

            </div>

            {workspaces.length === 0 ? (

              <div className="empty-state">

                <div style={{ fontSize: "36px" }}>
                  🏢
                </div>

                <p>
                  No workspaces yet.
                </p>

                <small>
                  Create your first workspace
                  to get started.
                </small>

              </div>

            ) : (

              <div className="workspace-list">

                {workspaces.map(
                  (workspace) => (

                    <div
                      className="workspace-card"
                      key={workspace.id}
                    >

                      <div className="workspace-card-top">

                        <div className="workspace-icon">
                          {workspace.name
                            .charAt(0)
                            .toUpperCase()}
                        </div>

                        <div>

                          <h3>
                            {workspace.name}
                          </h3>

                          <p>
                            {workspace.description ||
                              "Team workspace"}
                          </p>

                        </div>

                      </div>

                      <span className="workspace-id">
                        Workspace #{workspace.id}
                      </span>

                    </div>
                  )
                )}

              </div>

            )}

          </section>

        </div>

      </main>

    </div>
  );
}

export default Dashboard;