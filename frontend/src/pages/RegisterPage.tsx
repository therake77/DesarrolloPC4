import { useState } from "react";

export default function RegisterPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("SOLIDARIO");

  const handleRegister = async () => {
    const res = await fetch("http://localhost:8000/api/users/register", {
      method: "POST",
      body: JSON.stringify({
        name,
        email,
        password,
        role,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!res.ok) {
      console.log(res.statusText);
      return;
    }

    localStorage.setItem("caregiver_role", role);
    window.location.href = "/login";
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#f7fafc",
        padding: "24px",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "420px",
          background: "#ffffff",
          padding: "32px",
          borderRadius: "20px",
          boxShadow: "0 16px 40px rgba(15, 23, 42, 0.08)",
        }}
      >
        <h1 style={{ margin: 0, marginBottom: "24px", fontSize: "28px", textAlign: "center" }}>
          Regístrate
        </h1>

        <div style={{ display: "grid", gap: "18px" }}>
          <label style={{ display: "grid", gap: "8px", fontWeight: 600, color: "#1a202c" }}>
            Nombre
            <input
              type="text"
              placeholder="Nombre"
              value={name}
              onChange={(e) => setName(e.target.value)}
              style={{
                width: "100%",
                padding: "12px 14px",
                borderRadius: "12px",
                border: "1px solid #cbd5e1",
                fontSize: "16px",
              }}
            />
          </label>

          <label style={{ display: "grid", gap: "8px", fontWeight: 600, color: "#1a202c" }}>
            Email
            <input
              type="email"
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{
                width: "100%",
                padding: "12px 14px",
                borderRadius: "12px",
                border: "1px solid #cbd5e1",
                fontSize: "16px",
              }}
            />
          </label>

          <label style={{ display: "grid", gap: "8px", fontWeight: 600, color: "#1a202c" }}>
            Rol
            <select
              value={role}
              onChange={(e) => setRole(e.target.value)}
              style={{
                width: "100%",
                padding: "12px 14px",
                borderRadius: "12px",
                border: "1px solid #cbd5e1",
                fontSize: "16px",
                background: "#ffffff",
              }}
            >
              <option value="SOLIDARIO">Cuidador Solidario</option>
              <option value="PROFESIONAL">Profesional</option>
              <option value="ESPECIALIZADO">Especializado</option>
            </select>
          </label>

          <label style={{ display: "grid", gap: "8px", fontWeight: 600, color: "#1a202c" }}>
            Contraseña
            <input
              type="password"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                width: "100%",
                padding: "12px 14px",
                borderRadius: "12px",
                border: "1px solid #cbd5e1",
                fontSize: "16px",
              }}
            />
          </label>

          <button
            onClick={handleRegister}
            style={{
              width: "100%",
              padding: "14px 16px",
              borderRadius: "12px",
              border: "none",
              background: "#2b6cb0",
              color: "#ffffff",
              fontSize: "16px",
              fontWeight: 600,
              cursor: "pointer",
            }}
          >
            Regístrate
          </button>

          <p style={{ margin: 0, textAlign: "center", color: "#4a5568", fontSize: "14px" }}>
            ¿Tiene una cuenta?{' '}
            <a href="/login" style={{ color: "#2b6cb0", fontWeight: 600, textDecoration: "none" }}>
              Ingrese
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}
