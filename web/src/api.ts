const BASE = import.meta.env.VITE_API_BASE ?? '/api'

async function req<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(BASE + path, {
    headers: { 'Content-Type': 'application/json' },
    ...init,
  })
  if (!res.ok) throw new Error((await res.text()) || res.statusText)
  return res.json()
}

export const api = {
  health: () => req<{ status: string }>('/healthz'),
  models: (keyword?: string) =>
    req<{ count: number; models: any[] }>(`/models${keyword ? `?keyword=${keyword}` : ''}`),
  quant: (id: string, budget?: number) =>
    req<any>(`/quantize/${id}${budget ? `?budget_gb=${budget}` : ''}`),
  engines: () => req<{ engines: any[] }>('/serve/engines'),
  gpus: () => req<{ gpus: any[] }>('/cluster/gpus'),
  plan: (model_id: string, bits = 8) =>
    req<any>('/cluster/plan', { method: 'POST', body: JSON.stringify({ model_id, bits }) }),
  cost: (model_id: string, monthly_tokens_m = 100) =>
    req<any>('/cost/compare', {
      method: 'POST',
      body: JSON.stringify({ model_id, monthly_tokens_m }),
    }),
}
