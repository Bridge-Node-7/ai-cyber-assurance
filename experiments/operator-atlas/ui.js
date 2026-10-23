/* Operator Atlas Procedure Compass: browser-only research demonstrator */
"use strict";
(() => {
  const A = AtlasCore;
  const query = document.getElementById("search");
  const cards = document.getElementById("cards");
  const detail = document.getElementById("detail");
  const count = document.getElementById("count");
  const workspaces = new Map();
  let selectedId = A.recipes[0].id;
  function node(tag, text, className) {
    const n = document.createElement(tag);
    if (text !== undefined && text !== null) n.textContent = String(text);
    if (className) n.className = className;
    return n;
  }
  function append(parent, ...children) { for (const c of children) parent.appendChild(c); return parent; }
  function field(parent, title, value, change, kind = "text", placeholder = "") {
    const wrap = node("div", null, "field");
    const id = "oa-" + (++field.count);
    const lab = node("label", title); lab.htmlFor = id;
    const input = document.createElement("input"); input.id = id; input.type = kind;
    input.placeholder = placeholder; input.value = value || "";
    input.addEventListener("input", () => change(input.value));
    wrap.append(lab, input); parent.appendChild(wrap);
    return input;
  }
  field.count = 0;
  function choice(parent, title, val, values, change) {
    const wrap = node("div", null, "field");
    const id = "oa-" + (++field.count);
    const lab = node("label", title); lab.htmlFor = id;
    const select = node("select"); select.id = id;
    values.forEach(v => { const o = node("option", v); o.value = v; select.appendChild(o); });
    select.value = val || values[0];
    select.addEventListener("change", () => change(select.value));
    wrap.append(lab, select); parent.appendChild(wrap);
  }
  function workspace(id) {
    if (!workspaces.has(id)) {
      const r = A.recipes.find(x => x.id === id);
      workspaces.set(id, {authorized:false,scope:"",owner:"",reviewer:"",
        steps:r.steps.map(() => ({state:"unchecked",evidenceClass:"Unknown",reference:"",observedAt:""}))});
    }
    return workspaces.get(id);
  }
  function renderCards() {
    cards.replaceChildren();
    const results = A.searchRecipes(query.value, A.recipes);
    count.textContent = results.length + " curated procedure" + (results.length === 1 ? "" : "s");
    if (!results.length) cards.appendChild(node("div", "No match. Try identity, dependency, CVE, or AI agent.", "empty"));
    results.forEach(r => {
      const b = node("button", null, "task" + (selectedId === r.id ? " active" : ""));
      b.type = "button"; b.setAttribute("aria-pressed", String(selectedId === r.id));
      append(b, node("strong", r.title), node("small", r.short));
      b.addEventListener("click", () => { selectedId = r.id; renderCards(); renderDetail(); });
      cards.appendChild(b);
    });
  }
  function renderDetail() {
    detail.replaceChildren();
    const r = A.recipes.find(x => x.id === selectedId); if (!r) return;
    const w = workspace(r.id);
    append(detail,node("span", "GUIDED PROCEDURE · " + r.id.toUpperCase(), "eyebrow"),
      node("h2", r.title),node("p", r.short, "muted"));
    const metrics=node("div",null,"metrics");
    ["For: "+r.audience,"Applies: "+r.applies,"Reviewed: "+r.reviewedOn,
      A.freshnessOf(r.reviewedOn,new Date().toISOString().slice(0,10))].forEach(x=>metrics.appendChild(node("span",x,"chip")));
    detail.appendChild(metrics);
    detail.appendChild(node("div",r.risk+". Source dates do not guarantee procedure applicability. Verify service-specific instructions before action.","warn"));
    detail.appendChild(node("div",null,"divider"));
    detail.appendChild(node("h3","1 · Establish an authorized boundary","sectiontitle"));
    detail.appendChild(node("p","Use fictional or nonsensitive references. The page does not connect to your systems or independently validate entered evidence.","muted small"));
    const authorization=node("label",null,"checkboxline");
    const check=node("input");check.type="checkbox";check.checked=w.authorized;
    check.setAttribute("aria-label","I have authorization to conduct this scoped review");
    check.addEventListener("change",()=>{w.authorized=check.checked;updateStatus()});
    append(authorization,check,node("span","I confirm that I am authorized to review these systems. I will not use this prototype to store secrets or personal records."));
    detail.appendChild(authorization);
    const pair=node("div",null,"cols");
    field(pair,"Review scope / case label",w.scope,v=>{w.scope=v;updateStatus()},"text","Example: synthetic training environment");
    field(pair,"Accountable owner",w.owner,v=>{w.owner=v;updateStatus()},"text","Role or nonsensitive alias");
    detail.appendChild(pair);
    field(detail,"Named human reviewer",w.reviewer,v=>{w.reviewer=v;updateStatus()},"text","Reviewer's role or alias");
    detail.appendChild(node("div",null,"divider"));
    detail.appendChild(node("h3","2 · Check and record","sectiontitle"));
    detail.appendChild(node("p","A checkbox records an assertion, not proof. For each item, select a supported evidence class, reference and observation date. 'Reported' and 'Inferred' remain insufficient for review readiness.","muted small"));
    r.steps.forEach((step,i)=>{
      const s=w.steps[i];const item=node("section",null,"step");
      const head=node("div",null,"stephead");
      const title=node("div");append(title,node("h3",step.name),node("p",step.tip));
      append(head,node("span",String(i+1),"n"),title);item.appendChild(head);
      const cbLabel=node("label",null,"checkboxline");const cb=node("input");cb.type="checkbox";cb.checked=s.state==="checked";
      cb.setAttribute("aria-label","Checkpoint "+(i+1)+" checked");
      cb.addEventListener("change",()=>{s.state=cb.checked?"checked":"unchecked";updateStatus()});
      append(cbLabel,cb,node("span","I performed and recorded this check"));item.appendChild(cbLabel);
      const cols=node("div",null,"cols");
      choice(cols,"Evidence class",s.evidenceClass,["Unknown","Observed","Tested","Reported","Inferred"],v=>{s.evidenceClass=v;updateStatus()});
      field(cols,"Observation date",s.observedAt,v=>{s.observedAt=v;updateStatus()},"date");
      item.appendChild(cols);
      field(item,"Nonsensitive source or test reference",s.reference,v=>{s.reference=v;updateStatus()},"text","Example: SYN-LOG-001");
      detail.appendChild(item);
    });
    detail.appendChild(node("div",null,"divider"));
    detail.appendChild(node("h3","3 · Relevant original sources","sectiontitle"));
    const links=node("div",null,"links");
    r.sources.forEach(s=>{const link=node("a",s.title);link.href=s.url;link.target="_blank";link.rel="noopener noreferrer";links.appendChild(link)});
    detail.appendChild(links);
    detail.appendChild(node("div",null,"divider"));
    detail.appendChild(node("h3","4 · Review state and portable record","sectiontitle"));
    const box=node("div",null,"status wait");box.id="review-status";
    append(box,node("strong"),node("p"));detail.appendChild(box);
    const buttons=node("div",null,"actions");
    const exportBtn=node("button","Export declared review packet · JSON","btn");
    exportBtn.type="button";exportBtn.addEventListener("click",()=>download(r,w));
    const reset=node("button","Reset this session","btn secondary");reset.type="button";
    reset.addEventListener("click",()=>{workspaces.delete(r.id);renderDetail()});
    append(buttons,exportBtn,reset);detail.appendChild(buttons);
    detail.appendChild(node("p","Export contains editable user-declared entries. It is not signed, authenticated, or independently tested. Final action and risk acceptance remain with authorized humans.","muted small"));
    updateStatus();
  }
  function updateStatus() {
    const r=A.recipes.find(x=>x.id===selectedId); const status=A.assess(r,workspace(r.id));
    const box=document.getElementById("review-status");if(!box)return;
    const cls=status.status==="SAFE STOP"?"stop":status.status==="WAIT"?"wait":"ready";
    box.className="status "+cls;box.children[0].textContent=status.status;box.children[1].textContent=status.reason;
  }
  function download(r,w) {
    const status=A.assess(r,w);
    const packet={schema:"bn7.operator-atlas.declared-review.v0.2",generatedAt:new Date().toISOString(),
      provenance:"User-entered, editable, not verified by Operator Atlas",recipe:{id:r.id,title:r.title,reviewedOn:r.reviewedOn,sources:r.sources},
      case:{scope:w.scope,owner:w.owner,reviewer:w.reviewer,authorized:w.authorized},
      checks:r.steps.map((s,i)=>({step:s.name,...w.steps[i]})),
      procedureStatus:status.status,reason:status.reason,
      caveat:"This does not certify compliance, control effectiveness, operational readiness, access revocation, or human approval."};
    const blob=new Blob([JSON.stringify(packet,null,2)+"\n"],{type:"application/json"});
    const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;
    a.download="operator-atlas-"+r.id+"-declared-review.json";document.body.appendChild(a);a.click();a.remove();
    setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  query.addEventListener("input",renderCards);
  renderCards();renderDetail();
})();
