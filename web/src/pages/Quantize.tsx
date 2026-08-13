import { useEffect, useState } from 'react'
import { api } from '../api'
import Card from '../components/Card'
import Table from '../components/Table'

export default function Quantize() {
  const [models, setModels] = useState<any[]>([])
  const [sel, setSel] = useState('qwen/qwen3.8-2.4t-a95b')
  const [budget, setBudget] = useState('')
  const [result, setResult] = useState<any>(null)

  useEffect(() => {
    api.models().then((r) => setModels(r.models)).catch(console.error)
  }, [])

  async function run() {
    const r = await api.quant(sel, budget ? Number(budget) : undefined)
    setResult(r)
  }

  const rows = result
    ? result.results.map((q: any) => [
        q.method, `${q.bits}b`, `${q.quantized_gb}GB`,
        `${q.est_memory_gb}GB`, `${q.compression_ratio}x`,
        result.recommended === q.method ? '⭐ 推荐' : '',
      ])
    : []

  return (
    <div style={{ display: 'grid', gap: 16 }}>
      <Card title="量化方案估算">
        <div style={{ display: 'flex', gap: 10, flexWrap: 'wrap' }}>
          <select value={sel} onChange={(e) => setSel(e.target.value)}
            style={{ flex: 1, padding: 10, background: '#1d2430', color: '#e8ecf3', border: '1px solid #2a3342', borderRadius: 8 }}>
            {models.map((m) => (
              <option key={m.id} value={m.id}>{m.name}</option>
            ))}
          </select>
          <input placeholder="显存预算(GB) 可选" value={budget}
            onChange={(e) => setBudget(e.target.value)}
            style={{ width: 160, padding: 10, background: '#1d2430', color: '#e8ecf3', border: '1px solid #2a3342', borderRadius: 8 }} />
          <button onClick={run}
            style={{ padding: '10px 20px', background: '#e60012', color: '#fff', border: 'none', borderRadius: 8, cursor: 'pointer' }}>
            估算
          </button>
        </div>
      </Card>
      {result && (
        <Card title={`量化结果 — ${result.model}`} right={result.recommended ? `推荐：${result.recommended}` : undefined}>
          <Table columns={['方法', '比特', '磁盘', '显存', '压缩比', '']} rows={rows} />
        </Card>
      )}
    </div>
  )
}
