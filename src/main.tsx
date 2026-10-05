import React from "react";
import ReactDOM from "react-dom/client";
import "@fontsource-variable/instrument-sans";
import "@fontsource-variable/newsreader/opsz.css";
import "@fontsource/noto-serif-sc/400.css";
import "@fontsource/noto-serif-sc/600.css";
import "./styles.css";
import App from "./App";
import { Mascot, MascotProvider } from "./Mascot";
// Loaded last: Night Study v2 tokens and shared-spec layout.
import "./night.css";
class Boundary extends React.Component<
  React.PropsWithChildren,
  { failed: boolean }
> {
  state = { failed: false };
  static getDerivedStateFromError() {
    return { failed: true };
  }
  render() {
    return this.state.failed ? (
      <main className="recovery">
        <Mascot state="error" size={140} />
        <h1>Let’s get you back to learning.</h1>
        <p>
          Something interrupted the page. Your saved learning record stays on
          this device.
        </p>
        <button onClick={() => location.reload()}>Reload</button>
      </main>
    ) : (
      this.props.children
    );
  }
}
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Boundary>
      <MascotProvider><App /></MascotProvider>
    </Boundary>
  </React.StrictMode>,
);
