import { useEffect, useState } from 'react'
import { api } from '../api'
import Card from '../components/Card'
import Stat from '../components/Stat'

export default function Cost() {
  const [models, setModels] = useState<any[]>([])
  const [sel, setSel] = useState('deepseek/deepseek-v4-pro')
  const [tokens, setTokens] = useState('100')
  const [result, setResult] = useState<any>(null)

  useEffect(() => {
    api.models().then((r) => setModels(r.models)).catch(console.error)
  }, [])

  async function run() {
    const r = await api.cost(sel, Number(tokens))
    setResult(r)
  }

  return (
    <div style={{ display: 'grid', gap: 16 }}>
      <Card title="本地部署 vs 云端调用 成本对比">
        <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
          <select value={sel} onChange={(e) => setSel(e.target.value)}
            style={{ flex: 1, padding: 10, background: '#1d2430', color: '#e8ecf3', border: '1px solid #2a3342', borderRadius: 8 }}>
            {models.map((m) => <option key={m.id} value={m.id}>{m.name}</option>)}
          </select>
          <input placeholder="月用量(百万 token)" value={tokens}
            onChange={(e) => setTokens(e.target.value)}
            style={{ width: 180, padding: 10, background: '#1d2430', color: '#e8ecf3', border: '1px solid #2a3342', borderRadius: 8 }} />
          <button onClick={run} style={{ padding: '10px 20px', background: '#e60012', color: '#fff', border: 'none', borderRadius: 8, cursor: 'pointer' }}>
            对比
          </button>
        </div>
        {result && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(160px, 1fr))', gap: 12, marginTop: 16 }}>
            <Stat label="本地/月" value={`$${result.local_monthly_usd}`} />
            <Stat label="云端/月" value={`$${result.cloud_monthly_usd}`} />
            <Stat label="回本用量(M/月)" value={String(result.breakeven_tokens_m)} accent />
          </div>
        )}
        {result && <p style={{ marginTop: 16, color: 'var(--muted)' }}>{result.recommendation}</p>}
      </Card>
    </div>
  )
}
