#!/usr/bin/env python3
"""
Prefect UI에서 실행할 수 있도록 플로우 배포
"""
import os
from test_with_config import configured_server_flow

# Prefect 서버 설정
os.environ["PREFECT_API_URL"] = "http://localhost:4200/api"

def deploy_for_ui():
    """UI에서 실행 가능하도록 플로우 배포"""
    print("🚀 Prefect UI용 플로우 배포 중...")
    
    # 배포 생성
    deployment = configured_server_flow.to_deployment(
        name="UI-실행용-축산업-파이프라인",
        description="Prefect UI에서 버튼 클릭으로 실행 가능한 ML 파이프라인",
        version="1.0.0",
        tags=["ml", "livestock", "ui-executable"],
        # UI에서 수동 실행을 위해 스케줄 없음
        schedule=None,
        # 파라미터 설정 (UI에서 수정 가능)
        parameters={}
    )
    
    try:
        # 서버에 배포
        deployment_id = deployment.apply()
        
        print("✅ 배포 완료!")
        print(f"📊 Prefect UI: http://localhost:4200")
        print("📋 사용법:")
        print("1. Prefect UI (http://localhost:4200) 접속")
        print("2. 'Deployments' 탭 클릭")
        print("3. 'UI-실행용-축산업-파이프라인' 찾기")
        print("4. 'Quick Run' 버튼 클릭 → 실행!")
        print("5. 'Flow Runs' 탭에서 실행 상태 확인")
        
        return True
        
    except Exception as e:
        print(f"❌ 배포 실패: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Prefect UI 실행용 배포")
    print("=" * 60)
    
    success = deploy_for_ui()
    
    if success:
        print("\n🎉 이제 Prefect UI에서 버튼 클릭만으로 실행할 수 있습니다!")
    else:
        print("\n😞 배포 실패!")