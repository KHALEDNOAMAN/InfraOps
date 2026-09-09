import React from 'react';
import { Server, Zap, HardDrive, Cpu, AlertCircle, Calendar } from 'lucide-react';
import MetricCard from '../components/MetricCard';
import { PieChart, Pie, Cell, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Servers', value: 400 },
  { name: 'Switches', value: 50 },
  { name: 'Storage', value: 30 },
  { name: 'VMs', value: 800 },
];
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

const powerData = Array.from({length: 30}).map((_, i) => ({
  day: i + 1,
  kw: 100 + Math.random() * 20
}));

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <MetricCard icon={Server} label="Total Assets" value="1,280" trend={5} />
        <MetricCard icon={Zap} label="Avg Power Usage" value="112 kW" trend={-2} />
        <MetricCard icon={AlertCircle} label="Open Changes" value="14" trend={12} />
        <MetricCard icon={Cpu} label="CPU Utilization" value="68%" trend={3} />
        <MetricCard icon={HardDrive} label="Storage Used" value="74%" trend={8} />
        <MetricCard icon={Calendar} label="Expiring Licenses" value="3" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
          <h2 className="text-lg font-medium mb-4">Asset Distribution</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={data} innerRadius={60} outerRadius={80} paddingAngle={5} dataKey="value">
                  {data.map((entry, index) => <Cell key={index} fill={COLORS[index % COLORS.length]} />)}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
          <h2 className="text-lg font-medium mb-4">Power Consumption (30 Days)</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={powerData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="day" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: 'none' }} />
                <Line type="monotone" dataKey="kw" stroke="#22D3EE" strokeWidth={2} dot={false} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
