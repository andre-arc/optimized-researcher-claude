#!/usr/bin/env python3
import sys
import os
import json
import subprocess
import hashlib
import shutil
import platform
import glob

def ensure_uv_or_install():
    """Checks for uv and dynamically installs it using the official Astral script if missing."""
    if shutil.which("uv"):
        return "uv run"

    home = os.path.expanduser("~")
    possible_paths = [
        os.path.join(home, ".local", "bin", "uv"),
        os.path.join(home, ".cargo", "bin", "uv"),
        os.path.join(os.environ.get("APPDATA", ""), "astral-uv", "bin", "uv.exe")
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return f'"{path}" run'

    print("⚠️ 'uv' is not installed on this system.")
    current_os = platform.system().lower()

    try:
        if current_os == "windows":
            print("⚡ Launching official Astral UV installation via PowerShell...")
            ps_cmd = 'powershell -ExecutionPolicy ByPass -c "irm https://astral.sh | iex"'
            subprocess.run(ps_cmd, shell=True, check=True)
        else:
            print("⚡ Launching official Astral UV installation via curl...")
            curl_cmd = "curl -LsSf https://astral.sh | sh"
            subprocess.run(curl_cmd, shell=True, check=True)

        for path in possible_paths:
            if os.path.exists(path):
                return f'"{path}" run'
        if shutil.which("uv"):
            return "uv run"

    except Exception as e:
        print(f"⚠️ Native installation failed: {e}")

    print("💡 Falling back to standard Python engine execution pointer.")
    return sys.executable

def get_query_hash(query):
    return hashlib.md5(query.encode('utf-8')).hexdigest()

def main():
    # --- PHASE 1: DECOMPOSE SCOPE VIA SONNET ---
    if len(sys.argv) < 2:
        print("❌ Error: Missing target search topic.")
        sys.exit(1)

    main_topic = " ".join(sys.argv[1:])
    safe_filename = main_topic.lower().replace(' ', '_')

    execution_engine = ensure_uv_or_install()
    print(f"⚙️ Execution Engine locked: {execution_engine}")

    print(f"🔮 Prompt topic captured: '{main_topic}'")
    print("🧠 Requesting Claude 3.5 Sonnet to generate 5 optimal engineering search vectors...")

    generation_prompt = f"""
    Analyze this topic: "{main_topic}".
    Generate exactly 5 distinct, highly advanced engineering sub-angles to research.
    Ensure they map heavily to: core architectural bottlenecks, uncertainty gates, calibration, domain literature, and effect size trade-offs.

    Output ONLY a valid JSON dictionary where keys are short strings and values are the complete search query strings. No markdown formatting, no conversational text.
    Example format: {{"angle1": "query text 1", "angle2": "query text 2"}}
    """

    try:
        raw_output = subprocess.check_output(f"claude '{generation_prompt}'", shell=True, text=True)
        cleaned_json = raw_output.strip().strip("```json").strip("```")
        angles = json.loads(cleaned_json)
    except Exception as e:
        print(f"⚠️ Failed to parse dynamic angles. Falling back to default layout. Error: {e}")
        angles = {
            "angle_1": f"{main_topic} structural bottlenecks and implementation constraints",
            "angle_2": f"{main_topic} uncertainty mitigation and probability calibration",
            "angle_3": f"{main_topic} algorithmic optimization and math complexity thresholds",
            "angle_4": f"{main_topic} industry literature case studies and implementations",
            "angle_5": f"{main_topic} performance benchmarks and compute scaling trade-offs"
        }

    print("\n📐 Dynamic Angles Generated:")
    for key, val in angles.items():
        print(f"  [{key}]: {val}")

    cwd = os.getcwd()
    scratch_dir = os.path.join(cwd, ".claude", "scratchpad", "cache")
    output_dir = os.path.join(cwd, ".claude", "outputs")
    os.makedirs(scratch_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Proactively check workspace for any local PDF assets to inject into the research loop
    local_pdfs = glob.glob(os.path.join(cwd, "**", "*.pdf"), recursive=True)
    pdf_list_str = ", ".join([os.path.basename(p) for p in local_pdfs]) if local_pdfs else "None found"
    print(f"📂 Detected local workspace PDFs available for extraction: {pdf_list_str}")

    processes = []

    # --- PHASE 2 & 3: SEARCH, FETCH, AND PDF EXTRACT VIA PARALLEL HAIKU AGENTS ---
    print("\n📉 Dispatched ultra-lean parallel Haiku agents for web + PDF text extraction...")
    for angle_id, query in angles.items():
        cache_file = os.path.join(scratch_dir, f"{get_query_hash(query)}.json")

        if os.path.exists(cache_file):
            print(f"   📦 Cache hit for [{angle_id}]. Skipping extraction entirely.")
            continue

        prompt = f"""
        Execute an automated extraction task for research target: '{query}'.

        DATA GATHERING CHANNELS:
        1. Search and fetch standard web documents using `web-search` and `fetch-url`.
        2. Check this list of local workspace PDFs for relevant data: {local_pdfs}. If any match this search vector, read and extract text from them using the `view-file` tool.

        CRITICAL BUDGET CONSTRAINTS:
        - Max 10 data sources total (combined web pages and PDF extractions).
        - Stop reading each file or page asset at exactly 1,000 words. Completely ignore structural metadata.
        - Extract ONLY high-density, falsifiable claims.
        - Output the pure raw list as compact JSON to {cache_file}. Zero markdown formatting.
        """

        cmd = f"claude /bg /agent web-searcher '{prompt}'"
        processes.append(subprocess.Popen(cmd, shell=True))

    for p in processes:
        p.wait()

    # --- PHASE 4: ADVERSARIAL VERIFICATION VIA CLAUDE 3 OPUS ---
    print("\n🧠 Running 3-vote adversarial verification via Claude 3 Opus...")
    verified_claims_path = os.path.join(scratch_dir, "verified_claims.json")
    verification_prompt = f"""
    Analyze all JSON files inside the folder `{scratch_dir}` (except verified_claims.json if it exists).
    Cross-examine the raw web and PDF extracted data and perform a strict 3-vote adversarial verification check per claim.
    Compare contradictions and drop unverified generalizations or marketing fluff.

    Output ONLY a clean, verified JSON array of strict, falsifiable facts. Zero markdown.
    Write your output payload to: {verified_claims_path}
    """
    subprocess.run(f"claude --model opus '{verification_prompt}'", shell=True)

    # --- PHASE 5: ARCHITECTURAL SYNTHESIS VIA CLAUDE 3.5 SONNET ---
    print("💻 Generating optimized CPU vector pipeline via Claude 3.5 Sonnet...")
    output_manifest_path = os.path.join(output_dir, f"{safe_filename}_manifest.md")
    synthesis_prompt = f"""
    Read the validated claims list in `{verified_claims_path}`.
    Map these findings directly to a low-overhead, vectorized, CPU-only execution architecture (e.g., NumPy vectorized operations, structural memory packing).

    Generate a highly technical markdown engineering architecture report with code blocks at: {output_manifest_path}
    """
    subprocess.run(f"claude --model sonnet '{synthesis_prompt}'", shell=True)
    print(f"✅ Pipeline complete! Deep analysis report output written to: {output_manifest_path}")

if __name__ == "__main__":
    main()
