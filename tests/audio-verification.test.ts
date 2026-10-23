import { describe, expect, it } from "vitest";
import {
  independentAudioIssue,
  type IndependentProof,
} from "../scripts/audio-verification";

const proof: IndependentProof = {
  model: "Whisper large-v3",
  modelSha256: "pinned",
  rawSha256: "source",
  transcript: "把",
  status: "text-match",
  method: "Blind recognition",
};
const clip = {
  text: "把",
  rawSha256: "source",
  screeningStatus: "text-match",
  independentVerification: proof,
};
const evidence = {
  diagnosis: { model: proof.model, modelSha256: proof.modelSha256 },
  accepted: [{ text: clip.text, ...proof }],
};
describe("independent audio evidence", () => {
  it("accepts an exact source/model/transcript receipt", () =>
    expect(independentAudioIssue(clip, evidence)).toBeUndefined());
  it("leaves normal primary-screen recordings unchanged", () =>
    expect(independentAudioIssue({ text: "你好" })).toBeUndefined());
  it("rejects missing verification evidence", () =>
    expect(independentAudioIssue(clip)).toBeDefined());
  it.each([
    { rawSha256: "changed" },
    { modelSha256: "different-model" },
    { transcript: "八" },
    { status: "needs-review" },
  ])("rejects changed proof %j", (changed) => {
    expect(
      independentAudioIssue(
        { ...clip, independentVerification: { ...proof, ...changed } },
        evidence,
      ),
    ).toBeDefined();
  });
  it("cannot attach a valid receipt to another text", () =>
    expect(
      independentAudioIssue({ ...clip, text: "八" }, evidence),
    ).toBeDefined());
  it("rejects incomplete JSON proof", () => {
    const malformed = { ...proof } as Partial<IndependentProof>;
    delete malformed.transcript;
    expect(
      independentAudioIssue(
        { ...clip, independentVerification: malformed as IndependentProof },
        evidence,
      ),
    ).toBeDefined();
  });
});
