import { useEffect, useState } from 'react'
import { api } from '../api'
import Card from '../components/Card'
import Table from '../components/Table'
import SearchBar from '../components/SearchBar'
import Tag from '../components/Tag'

export default function Models() {
  const [models, setModels] = useState<any[]>([])
  const [kw, setKw] = useState('')

  useEffect(() => {
    api.models(kw || undefined).then((r) => setModels(r.models)).catch(console.error)
  }, [kw])

  const rows = models.map((m) => [
    m.id,
    m.name,
    <Tag color={m.architecture === 'moe' ? '#5b2a86' : '#1f6f5f'}>{m.architecture}</Tag>,
    m.total_params_b ? `${m.total_params_b}B` : '-',
    m.active_params_b ? `${m.active_params_b}B` : '-',
    m.bf16_size_gb ? `${m.bf16_size_gb}GB` : '-',
    m.license,
  ])

  return (
    <div style={{ display: 'grid', gap: 16 }}>
      <SearchBar value={kw} onChange={setKw} />
      <Card title={`开源模型库（${models.length}）`}>
        <Table
          columns={['ID', '名称', '架构', '总参数', '激活参数', '体积', 'License']}
          rows={rows}
        />
      </Card>
    </div>
  )
}
