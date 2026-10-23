export type IndependentProof = {
  model: string;
  modelSha256: string;
  rawSha256: string;
  transcript: string;
  status: string;
  method: string;
};
export type VerificationEvidence = {
  diagnosis: { model: string; modelSha256: string };
  accepted: (IndependentProof & { text: string })[];
};
export function independentAudioIssue(
  clip: {
    text?: string;
    rawSha256?: string;
    screeningStatus?: string;
    independentVerification?: IndependentProof;
  },
  evidence?: VerificationEvidence,
): string | undefined {
  const proof = clip.independentVerification;
  if (!proof) return;
  const saved = evidence?.accepted.find(
    (row) => row.text === clip.text && row.rawSha256 === clip.rawSha256,
  );
  if (!saved || !evidence) return "Independent verification receipt missing";
  if (
    proof.model !== evidence.diagnosis.model ||
    proof.modelSha256 !== evidence.diagnosis.modelSha256
  )
    return "Independent recognizer does not match its pinned model";
  if (
    proof.rawSha256 !== clip.rawSha256 ||
    proof.status !== clip.screeningStatus
  )
    return "Independent verification does not match this source and status";
  if (
    ![
      "text-match",
      "homophone-transcript",
      "erhua-transcript",
      "phone-number-transcript",
    ].includes(proof.status)
  )
    return "Independent result did not pass the phonetic screen";
  const required: (keyof IndependentProof)[] = [
    "model",
    "modelSha256",
    "rawSha256",
    "transcript",
    "status",
    "method",
  ];
  for (const key of required)
    if (
      typeof proof[key] !== "string" ||
      !proof[key] ||
      proof[key] !== saved[key]
    )
      return "Independent evidence changed";
}
