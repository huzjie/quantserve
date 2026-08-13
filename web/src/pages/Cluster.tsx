import { useEffect, useState } from 'react'
import { api } from '../api'
import Card from '../components/Card'
import Stat from '../components/Stat'

export default function Cluster() {
  const [gpus, setGpus] = useState<any[]>([])
  const [models, setModels] = useState<any[]>([])
  const [sel, setSel] = useState('qwen/qwen3.8-2.4t-a95b')
  const [plan, setPlan] = useState<any>(null)

  useEffect(() => {
    api.gpus().then((r) => setGpus(r.gpus)).catch(console.error)
    api.models().then((r) => setModels(r.models)).catch(console.error)
  }, [])

  async function run() {
    const r = await api.plan(sel, 8)
    setPlan(r)
  }

  return (
    <div style={{ display: 'grid', gap: 16 }}>
      <Card title="GPU 集群">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', gap: 12 }}>
          {gpus.length === 0 && <p style={{ color: 'var(--muted)' }}>未检测到 GPU（需 nvidia-smi）</p>}
          {gpus.map((g) => (
            <div key={g.index} style={{ background: 'var(--panel-2)', padding: 14, borderRadius: 8 }}>
              <div style={{ fontWeight: 700 }}>{g.name}</div>
              <div style={{ color: 'var(--muted)', fontSize: 12 }}>{g.memory_gb}GB · CC {g.compute_capability}</div>
            </div>
          ))}
        </div>
      </Card>
      <Card title="并行策略规划">
        <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
          <select value={sel} onChange={(e) => setSel(e.target.value)}
            style={{ flex: 1, padding: 10, background: '#1d2430', color: '#e8ecf3', border: '1px solid #2a3342', borderRadius: 8 }}>
            {models.map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}
          </select>
          <button onClick={run} style={{ padding: '10px 20px', background: '#e60012', color: '#fff', border: 'none', borderRadius: 8, cursor: 'pointer' }}>
            规划
          </button>
        </div>
        {plan?.plan && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(140px, 1fr))', gap: 12, marginTop: 16 }}>
            <Stat label="Tensor Parallel" value={String(plan.plan.details.tensor_parallel)} />
            <Stat label="Expert Parallel" value={String(plan.plan.details.expert_parallel)} />
            <Stat label="Data Parallel" value={String(plan.plan.details.data_parallel)} />
            <Stat label="GPU 数" value={String(plan.plan.details.gpu_count)} accent />
          </div>
        )}
      </Card>
    </div>
  )
}
