import { useState } from "react";
import { AppleLogo, ArrowLeft, EnvelopeSimple } from "@phosphor-icons/react";
import {
  authConfigured,
  emailConfigured,
  oauthConfigured,
  sendEmailCode,
  signInWith,
  verifyEmailCode,
  type OAuthProvider,
} from "./auth";
import { BrandSignature, brand } from "./brand";
import { Arrow } from "./components";
import { MoSays } from "./Mascot";
import { welcomeGreeting as greeting } from "./sayo-lines";
import type { Account } from "./types";

/** Multi-colour Google "G", per Google's sign-in button guidance. */
function GoogleG() {
  return (
    <svg width="18" height="18" viewBox="0 0 48 48" aria-hidden>
      <path
        fill="#EA4335"
        d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"
      />
      <path
        fill="#4285F4"
        d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"
      />
      <path
        fill="#FBBC05"
        d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"
      />
      <path
        fill="#34A853"
        d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"
      />
    </svg>
  );
}

/**
 * The first screen: Sayo says hello, then the learner signs in or simply starts.
 * Nothing here blocks learning; an account can be added later in Settings.
 */
export default function Welcome({
  onAccount,
  onGuest,
}: {
  onAccount: (account: Account) => Promise<void>;
  onGuest: () => Promise<void>;
}) {
  const [stage, setStage] = useState<"choose" | "email" | "code">("choose"),
    [email, setEmail] = useState(""),
    [code, setCode] = useState(""),
    [busy, setBusy] = useState<string | null>(null),
    [error, setError] = useState(""),
    [notice, setNotice] = useState("");
  const run = async (label: string, task: () => Promise<void>) => {
    setBusy(label);
    setError("");
    try {
      await task();
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(null);
    }
  };
  const oauth = (p: OAuthProvider) => run(p, () => signInWith(p));
  const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.trim());
  return (
    <main className="welcome">
      <div className="welcome-stage" aria-hidden={false}>
        <MoSays
          state="welcome"
          say={greeting}
          size={320}
          side="top"
          showcase
          className="welcome-mo"
        />
      </div>
      <section className="welcome-panel" aria-labelledby="welcome-title">
        <div className="welcome-brand">
          <BrandSignature />
        </div>
        <h1 id="welcome-title">{brand.tagline}</h1>
        <p className="lede">
          Read it, hear it, say it, starting from your very first 一. Short
          lessons, real Chinese, and a mentor who doesn’t let tones slide.
        </p>

        {stage === "choose" && (
          <div className="auth-options">
            {emailConfigured && (
              <button
                className="auth-button apple"
                disabled={!oauthConfigured("apple") || busy !== null}
                title={
                  oauthConfigured("apple")
                    ? undefined
                    : "Apple sign-in is not configured. Use email."
                }
                onClick={() => void oauth("apple")}
              >
                <AppleLogo size={20} weight="fill" />
                {busy === "apple" ? "Opening Apple…" : "Continue with Apple"}
              </button>
            )}
            <button
              className="auth-button google"
              disabled={!oauthConfigured("google") || busy !== null}
              title={
                oauthConfigured("google")
                  ? undefined
                  : "Google sign-in is not configured yet."
              }
              onClick={() => void oauth("google")}
            >
              <GoogleG />
              {busy === "google" ? "Opening Google…" : "Continue with Google"}
            </button>
            {emailConfigured && (
              <button
                className="auth-button email"
                disabled={!authConfigured || busy !== null}
                onClick={() => setStage("email")}
              >
                <EnvelopeSimple size={20} />
                Continue with email
              </button>
            )}
            {authConfigured && !emailConfigured && (
              <p className="auth-note">
                Private sync · the owner’s Google account only.
              </p>
            )}
            {!authConfigured && (
              <p className="auth-note" role="note">
                Accounts aren’t switched on yet. You can start now and add one
                later from Settings.
              </p>
            )}
          </div>
        )}

        {stage === "email" && (
          <form
            className="auth-form"
            onSubmit={(e) => {
              e.preventDefault();
              if (!validEmail) return;
              void run("send", async () => {
                await sendEmailCode(email.trim());
                setNotice(
                  `Check ${email.trim()} and open the sign-in link in this browser. If the email includes a code, enter it below.`,
                );
                setStage("code");
              });
            }}
          >
            <label className="field">
              Email
              <input
                type="email"
                inputMode="email"
                autoComplete="email"
                autoFocus
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
              />
            </label>
            <div className="auth-row">
              <button
                type="button"
                className="text-button"
                onClick={() => setStage("choose")}
              >
                <ArrowLeft size={17} /> Other options
              </button>
              <button
                className="button"
                disabled={!validEmail || busy !== null}
              >
                {busy === "send" ? "Sending…" : "Send sign-in email"} <Arrow />
              </button>
            </div>
          </form>
        )}

        {stage === "code" && (
          <form
            className="auth-form"
            onSubmit={(e) => {
              e.preventDefault();
              void run("verify", async () =>
                onAccount(await verifyEmailCode(email.trim(), code)),
              );
            }}
          >
            <p className="auth-sent" role="status">
              {notice}
            </p>
            <label className="field">
              Email code (if provided)
              <input
                className="code-input"
                inputMode="numeric"
                autoComplete="one-time-code"
                autoFocus
                maxLength={12}
                value={code}
                onChange={(e) => setCode(e.target.value.replace(/\D/g, ""))}
                placeholder="••••••"
              />
            </label>
            <div className="auth-row">
              <button
                type="button"
                className="text-button"
                onClick={() => setStage("email")}
              >
                <ArrowLeft size={17} /> Change email
              </button>
              <button
                className="button"
                disabled={!code.trim() || busy !== null}
              >
                {busy === "verify" ? "Checking…" : "Sign in"} <Arrow />
              </button>
            </div>
          </form>
        )}

        {error && (
          <p className="inline-error" role="alert">
            {error}
          </p>
        )}

        <div className="auth-divider" role="separator">
          <span>or</span>
        </div>
        <button
          className={authConfigured ? "guest-button" : "button guest-primary"}
          disabled={busy !== null}
          onClick={() => void run("guest", onGuest)}
        >
          Start without an account <Arrow />
        </button>
        <p className="small auth-fineprint">
          Study history stays available in this browser. When cloud sync is
          connected, you choose whether to add this device’s progress to your
          account.
        </p>
      </section>
    </main>
  );
}
