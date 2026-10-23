/* Operator Atlas experiment v0.2 — synthetic/public-safe reference only */
const AtlasCore = (() => {
  const recipes = [
  {
    "id": "offboarding",
    "title": "Verify contractor access is removed",
    "short": "Cross-check identity, application, privileged, token, and session boundaries after offboarding.",
    "tags": [
      "offboard",
      "contractor",
      "identity",
      "SSO",
      "ICAM",
      "access",
      "sessions"
    ],
    "audience": "IT and identity administrators",
    "applies": "Authorized organization-owned identity and application systems",
    "reviewedOn": "2026-10-23",
    "risk": "Approval required for live changes",
    "sources": [
      {
        "title": "NIST SP 800-63B-4 — Session Management",
        "url": "https://pages.nist.gov/800-63-4/sp800-63b/session/"
      },
      {
        "title": "NIST SP 800-63C-4 — General-Purpose IdP",
        "url": "https://pages.nist.gov/800-63-4/sp800-63c/GenIdP/"
      }
    ],
    "steps": [
      {
        "name": "Declare owner, cutoff, and authorized review scope",
        "tip": "Record system boundaries and the authoritative offboarding event. Do not place personal data in this demo."
      },
      {
        "name": "Check identity-provider and directory account state",
        "tip": "Use approved administration views or sanitized exports. Record the actual observation timestamp."
      },
      {
        "name": "Check application-local and privileged access",
        "tip": "SSO deactivation does not establish application-local account removal or role revocation."
      },
      {
        "name": "Check active sessions, tokens, and non-human access",
        "tip": "Confirm service-specific revocation behavior; an IdP logout may leave downstream sessions active."
      },
      {
        "name": "Review exceptions and arrange independent retest",
        "tip": "Assign required changes to authorized administrators; recheck after changes and retain accountable human review."
      }
    ]
  },
  {
    "id": "dependency",
    "title": "Triage a vulnerable dependency",
    "short": "Decide whether a vulnerability requires investigation for a particular software version and environment.",
    "tags": [
      "CVE",
      "dependency",
      "package",
      "OSV",
      "KEV",
      "EPSS",
      "triage"
    ],
    "audience": "Software maintainers and security analysts",
    "applies": "Verified software inventories, version data, and vendor advisories",
    "reviewedOn": "2026-10-23",
    "risk": "Do not infer exposure from CVE presence alone",
    "sources": [
      {
        "title": "CISA Known Exploited Vulnerabilities",
        "url": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
      },
      {
        "title": "OSV open-source vulnerability database",
        "url": "https://osv.dev/"
      },
      {
        "title": "FIRST EPSS overview",
        "url": "https://www.first.org/epss/"
      }
    ],
    "steps": [
      {
        "name": "Identify exact product, package, and installed version",
        "tip": "Record a sanitized inventory reference, not secrets or private asset lists."
      },
      {
        "name": "Confirm affected ranges and advisory status",
        "tip": "Read vendor and OSV advisories. Applicability depends on actual versions and configuration."
      },
      {
        "name": "Check exploitation signals without confusing metrics",
        "tip": "KEV indicates known exploitation evidence; EPSS is a forecast, not an incident report."
      },
      {
        "name": "Examine exposure and compensating controls",
        "tip": "Record reachability, feature use, controls, and uncertainties rather than assuming the asset is affected."
      },
      {
        "name": "Assign remediation and schedule revalidation",
        "tip": "Capture patch/mitigation plan and evidence required for a later verified outcome."
      }
    ]
  },
  {
    "id": "agent",
    "title": "Inspect an AI agent's authority boundaries",
    "short": "Make tool permissions, identities, data movement, approval gates, and rollback visible before an agent acts.",
    "tags": [
      "AI",
      "agent",
      "tools",
      "permissions",
      "human",
      "boundary",
      "identity"
    ],
    "audience": "AI builders, cybersecurity and governance teams",
    "applies": "Declared agent configurations and authorized synthetic or isolated tests",
    "reviewedOn": "2026-10-23",
    "risk": "No production tool execution or privilege modification",
    "sources": [
      {
        "title": "NIST AI Risk Management Framework",
        "url": "https://www.nist.gov/itl/ai-risk-management-framework"
      },
      {
        "title": "OWASP GenAI Security Project",
        "url": "https://genai.owasp.org/"
      }
    ],
    "steps": [
      {
        "name": "Inventory tool access and execution identities",
        "tip": "Identify tokens, principals, service accounts and tool scopes without exposing credentials."
      },
      {
        "name": "Map data trust boundaries",
        "tip": "Distinguish untrusted retrieval content from authoritative instructions and secret-bearing sources."
      },
      {
        "name": "Define consequential-action human gates",
        "tip": "Record who authorizes access changes, payments, external communication, and production changes."
      },
      {
        "name": "Run isolated negative tests",
        "tip": "Use mock endpoints to test denied operations and scope escalation; do not probe live services."
      },
      {
        "name": "Document kill switch, rollback, and monitoring",
        "tip": "Identify owner and disable mechanism; a documented rollback is not a successful rollback test."
      }
    ]
  }
];
  function searchRecipes(query, pool){const words=String(query||"").toLowerCase().trim().split(/\s+/).filter(Boolean);return pool.map(r=>{const hay=[r.title,r.short,r.audience,...r.tags].join(" ").toLowerCase();const score=words.reduce((n,w)=>n+(r.title.toLowerCase().includes(w)?5:0)+(r.tags.some(t=>t.toLowerCase().includes(w))?3:0)+(hay.includes(w)?1:0),0);return{recipe:r,score}}).filter(x=>!words.length||x.score>0).sort((a,b)=>b.score-a.score||a.recipe.title.localeCompare(b.recipe.title)).map(x=>x.recipe)}
  function freshnessOf(date,today){const a=Date.parse(date+"T00:00:00Z"),b=Date.parse(today+"T00:00:00Z");if(!Number.isFinite(a)||!Number.isFinite(b)||a>b)return"UNKNOWN";return(b-a)/(86400000)>180?"REVIEW DUE":"DATED REFERENCE"}
  function assess(recipe,work){if(!work||work.authorized!==true)return{status:"SAFE STOP",reason:"Authorization or scope not confirmed; do not continue with live-system testing."};if(!String(work.scope||"").trim()||!String(work.owner||"").trim())return{status:"WAIT",reason:"A bounded scope and named owner are required."};if(!String(work.reviewer||"").trim())return{status:"WAIT",reason:"A named human reviewer is required."};if(!Array.isArray(work.steps)||work.steps.length!==recipe.steps.length)return{status:"WAIT",reason:"Not all procedure checkpoints have been recorded."};for(let i=0;i<recipe.steps.length;i++){const s=work.steps[i]||{};if(s.state!=="checked"||!["Observed","Tested"].includes(s.evidenceClass)||!String(s.reference||"").trim()||!String(s.observedAt||"").trim())return{status:"WAIT",reason:`Checkpoint ${i+1} lacks a completed check with Observed/Tested evidence reference and observation date.`}}return{status:"READY FOR HUMAN REVIEW",reason:"All declared checkpoints have traceable entries; this is not independent validation, certification, or operational approval."}}
  return Object.freeze({recipes,searchRecipes,freshnessOf,assess});
})();
if (typeof module !== "undefined" && module.exports) module.exports = AtlasCore;
